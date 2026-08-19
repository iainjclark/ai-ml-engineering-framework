"""
Runtime diagnostics.

Collects dynamic information about system and process resource usage while
a workload is executing.

This module provides:

    get_runtime_diagnostics()
        Capture an instantaneous snapshot of system and current-process
        resource usage.

    TaskMonitor
        Monitor the current Python process while a task executes, recording
        elapsed time, process CPU time, memory consumption and related
        runtime metrics.

Runtime diagnostics are:

    runtime.py
        What resources are being consumed during execution?

Runtime diagnostics are intentionally distinct from:

    hardware.py
        What physical machine am I running on?

    environment.py
        What operating environment am I running in?

"""

from __future__ import annotations

import os
import statistics
import threading
import time
from typing import Any

import psutil


def _bytes_to_mb(value: int | float) -> float:
    """Convert bytes to MiB."""
    return round(value / (1024 ** 2), 2)


def get_system_usage() -> dict[str, Any]:
    """
    Return an instantaneous snapshot of system-wide resource usage.
    """
    cpu_per_core = psutil.cpu_percent(percpu=True)
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()

    return {
        "CPU": {
            "Overall Usage (%)": psutil.cpu_percent(),
            "Per Core Usage (%)": cpu_per_core,
            "Logical CPUs": psutil.cpu_count(logical=True),
        },
        "Memory": {
            "Total (MB)": _bytes_to_mb(memory.total),
            "Available (MB)": _bytes_to_mb(memory.available),
            "Used (MB)": _bytes_to_mb(memory.used),
            "Usage (%)": memory.percent,
        },
        "Swap": {
            "Total (MB)": _bytes_to_mb(swap.total),
            "Used (MB)": _bytes_to_mb(swap.used),
            "Usage (%)": swap.percent,
        },
    }


def get_process_usage() -> dict[str, Any]:
    """
    Return an instantaneous snapshot of the current Python process.
    """
    process = psutil.Process(os.getpid())

    memory = process.memory_info()
    cpu_times = process.cpu_times()

    try:
        io = process.io_counters()
        io_info = {
            "Read Bytes": io.read_bytes,
            "Write Bytes": io.write_bytes,
        }
    except (psutil.AccessDenied, AttributeError, NotImplementedError):
        io_info = None

    return {
        "PID": process.pid,
        "CPU": {
            "User Time (s)": round(cpu_times.user, 4),
            "System Time (s)": round(cpu_times.system, 4),
            "Total CPU Time (s)": round(
                cpu_times.user + cpu_times.system,
                4,
            ),
        },
        "Memory": {
            "RSS (MB)": _bytes_to_mb(memory.rss),
            "VMS (MB)": _bytes_to_mb(memory.vms),
            "Memory Usage (%)": round(
                process.memory_percent(),
                4,
            ),
        },
        "Threads": process.num_threads(),
        "IO": io_info,
    }


def get_runtime_diagnostics() -> dict[str, Any]:
    """
    Capture an instantaneous runtime diagnostic snapshot.
    """
    return {
        "System": get_system_usage(),
        "Process": get_process_usage(),
    }


class TaskMonitor:
    """
    Monitor resource usage by the current Python process during a task.

    Example
    -------
    >>> with TaskMonitor("model_training") as monitor:
    ...     train_model()
    ...
    >>> print(monitor.metrics)

    Notes
    -----
    CPU utilisation may exceed 100% when the process is using more than
    one logical CPU.

    Peak memory is obtained by periodic sampling, so extremely short-lived
    memory spikes may not be observed.
    """

    def __init__(
        self,
        task_name: str,
        sample_interval: float = 0.1,
    ) -> None:
        if sample_interval <= 0:
            raise ValueError("sample_interval must be greater than zero")

        self.task_name = task_name
        self.sample_interval = sample_interval

        self.process = psutil.Process(os.getpid())

        self.metrics: dict[str, Any] = {}

        self._stop_event = threading.Event()
        self._sampling_thread: threading.Thread | None = None

        self._rss_samples: list[int] = []
        self._cpu_samples: list[float] = []

        self._start_wall: float | None = None
        self._start_cpu: float | None = None

        self._start_rss: int | None = None
        self._start_threads: int | None = None
        self._start_io: Any = None

    def _sample(self) -> None:
        """Take one process resource sample."""
        try:
            self._rss_samples.append(
                self.process.memory_info().rss
            )

            self._cpu_samples.append(
                self.process.cpu_percent(interval=None)
            )

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    def _sampling_loop(self) -> None:
        """Periodically collect process resource samples."""
        while not self._stop_event.is_set():
            self._sample()
            self._stop_event.wait(self.sample_interval)

    def __enter__(self) -> "TaskMonitor":
        self._stop_event.clear()
        self._rss_samples.clear()
        self._cpu_samples.clear()

        cpu_times = self.process.cpu_times()

        self._start_cpu = cpu_times.user + cpu_times.system
        self._start_wall = time.perf_counter()

        self._start_rss = self.process.memory_info().rss
        self._start_threads = self.process.num_threads()

        try:
            self._start_io = self.process.io_counters()
        except (
            psutil.AccessDenied,
            AttributeError,
            NotImplementedError,
        ):
            self._start_io = None

        # Initialise psutil's process CPU measurement.
        self.process.cpu_percent(interval=None)

        self._sampling_thread = threading.Thread(
            target=self._sampling_loop,
            daemon=True,
        )
        self._sampling_thread.start()

        return self

    def __exit__(
        self,
        exc_type: Any,
        exc_value: Any,
        traceback: Any,
    ) -> None:
        self._stop_event.set()

        if self._sampling_thread is not None:
            self._sampling_thread.join(
                timeout=self.sample_interval * 2
            )

        # Ensure a final resource sample is captured.
        self._sample()

        end_wall = time.perf_counter()

        cpu_times = self.process.cpu_times()
        end_cpu = cpu_times.user + cpu_times.system

        end_memory = self.process.memory_info()
        end_threads = self.process.num_threads()

        wall_time = (
            end_wall - self._start_wall
            if self._start_wall is not None
            else None
        )

        cpu_time = (
            end_cpu - self._start_cpu
            if self._start_cpu is not None
            else None
        )

        start_rss = self._start_rss or end_memory.rss

        peak_rss = max(
            self._rss_samples,
            default=end_memory.rss,
        )

        io_metrics = None

        try:
            end_io = self.process.io_counters()

            if self._start_io is not None:
                io_metrics = {
                    "Read Bytes": (
                        end_io.read_bytes
                        - self._start_io.read_bytes
                    ),
                    "Write Bytes": (
                        end_io.write_bytes
                        - self._start_io.write_bytes
                    ),
                }

        except (
            psutil.AccessDenied,
            AttributeError,
            NotImplementedError,
        ):
            pass

        cpu_samples = [
            value
            for value in self._cpu_samples
            if value >= 0
        ]

        self.metrics = {
            "Task": self.task_name,
            "Status": (
                "Completed"
                if exc_type is None
                else "Failed"
            ),
            "Timing": {
                "Wall Time (s)": (
                    round(wall_time, 4)
                    if wall_time is not None
                    else None
                ),
                "Process CPU Time (s)": (
                    round(cpu_time, 4)
                    if cpu_time is not None
                    else None
                ),
            },
            "CPU": {
                "Mean Process Usage (%)": (
                    round(
                        statistics.mean(cpu_samples),
                        2,
                    )
                    if cpu_samples
                    else None
                ),
                "Peak Process Usage (%)": (
                    round(max(cpu_samples), 2)
                    if cpu_samples
                    else None
                ),
            },
            "Memory": {
                "Start RSS (MB)": _bytes_to_mb(
                    start_rss
                ),
                "End RSS (MB)": _bytes_to_mb(
                    end_memory.rss
                ),
                "Peak RSS (MB)": _bytes_to_mb(
                    peak_rss
                ),
                "RSS Change (MB)": _bytes_to_mb(
                    end_memory.rss - start_rss
                ),
            },
            "Threads": {
                "Start": self._start_threads,
                "End": end_threads,
            },
            "IO": io_metrics,
        }


if __name__ == "__main__":
    from pprint import pprint

    print("Instantaneous runtime diagnostics:")
    pprint(get_runtime_diagnostics())

    print("\nTask monitoring example:")

    with TaskMonitor("example_task") as monitor:
        sum(i * i for i in range(5_000_000))

    pprint(monitor.metrics)
