"""
Execution environment diagnostics.

Collects information describing the operating environment in which an
AI/ML workload is executing.

This module is intentionally distinct from hardware diagnostics:

    hardware.py
        What physical machine am I running on?

    environment.py
        What operating environment am I running in?

Initial implementation refactored from the MachineDiagnostics notebook.
"""

from __future__ import annotations

import os
import platform
import psutil
import socket
import subprocess

from typing import Any

from ._shell import _run_command

def get_container_info() -> dict[str, object]:
    """
    Detect whether the current process is running inside a container.

    Returns container/orchestrator information where it can be determined.
    """
    if platform.system() != "Linux":
        return {
            "Detected": False,
            "Type": None,
        }

    # Kubernetes is an orchestrator rather than a container runtime,
    # so detect it first and report it as such.
    kubernetes = (
        "KUBERNETES_SERVICE_HOST" in os.environ
        or os.path.exists(
            "/var/run/secrets/kubernetes.io/serviceaccount"
        )
    )

    container_type = None

    # Preferred Linux/systemd mechanism when available.
    detected = _run_command(
        ["systemd-detect-virt", "--container"]
    )

    if detected and detected != "none":
        container_type = detected

    # Additional fallbacks.
    if container_type is None and os.path.exists("/.dockerenv"):
        container_type = "docker"

    if container_type is None:
        try:
            with open(
                "/proc/1/cgroup",
                encoding="utf-8",
            ) as cgroup_file:
                cgroup = cgroup_file.read().lower()

            if "docker" in cgroup:
                container_type = "docker"
            elif "kubepods" in cgroup:
                container_type = "container"
            elif "containerd" in cgroup:
                container_type = "containerd"
            elif "lxc" in cgroup:
                container_type = "lxc"

        except OSError:
            pass

    is_container = container_type is not None or kubernetes

    if kubernetes:
        display_type = (
            f"Kubernetes ({container_type})"
            if container_type
            else "Kubernetes"
        )
    else:
        display_type = container_type

    return {
        "Detected": is_container,
        "Type": display_type,
    }


def get_container_storage_info(
    container: dict[str, Any],
) -> dict[str, Any] | None:
    """Return the root filesystem visible to a container."""
    if not container.get("Detected"):
        return None

    try:
        usage = psutil.disk_usage("/")
        partitions = psutil.disk_partitions(all=True)

        root_partition = next(
            (
                partition
                for partition in partitions
                if partition.mountpoint == "/"
            ),
            None,
        )
        return {
            "Mount Point": "/",
            "Device": (
                root_partition.device
                if root_partition
                else None
            ),
            "File System": (
                root_partition.fstype
                if root_partition
                else None
            ),
            "Size (Bytes)": usage.total,
            "Available (Bytes)": usage.free,
        }

    except (OSError, PermissionError):
        return None

def _get_linux_distribution() -> str:
    """Return the Linux distribution name using freedesktop os-release."""
    try:
        os_release = platform.freedesktop_os_release()

        return os_release.get(
            "PRETTY_NAME",
            os_release.get("NAME", "Linux"),
        )

    except OSError:
        return "Linux"

def get_os_info() -> dict[str, Any]:
    """Return operating-system and platform information."""
    uname = platform.uname()
    system = platform.system()

    info = {
        "System": system,
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Node": uname.node,
    }

    if system == "Linux":
        info["Distribution"] = _get_linux_distribution()
    elif system == "Darwin":
        mac_version = platform.mac_ver()[0]
        info["Distribution"] = (
            f"macOS {mac_version}"
            if mac_version
            else "macOS"
        )
        info["Kernel"] = f"Darwin {platform.release()}"

    return info

def get_host_info() -> dict[str, Any]:
    """
    Return basic host identity information.

    Hostname is useful for distinguishing execution environments but should
    not be treated as a globally unique machine identifier.
    """
    try:
        hostname = socket.gethostname()
    except Exception:
        hostname = "Unknown"

    try:
        fqdn = socket.getfqdn()
    except Exception:
        fqdn = "Unknown"

    return {
        "Hostname": hostname,
        "FQDN": fqdn,
    }


def get_architecture_info() -> dict[str, Any]:
    """
    Return information about the operating-system/Python architecture.
    """
    bits, linkage = platform.architecture()

    return {
        "Architecture": bits,
        "Linkage": linkage,
        "Machine": platform.machine(),
    }


def get_python_runtime_info() -> dict[str, Any]:
    """
    Return information about the Python interpreter executing the workload.

    Detailed installed-package information belongs in software.py; this
    function records only the interpreter/runtime itself.
    """
    return {
        "Implementation": platform.python_implementation(),
        "Version": platform.python_version(),
        "Compiler": platform.python_compiler(),
        "Build": platform.python_build(),
        "Executable": os.path.abspath(os.sys.executable),
    }

def get_environment_diagnostics() -> dict[str, Any]:
    """Capture execution-environment diagnostics."""
    container = get_container_info()

    return {
        "Host": get_host_info(),
        "Operating System": get_os_info(),
        "Architecture": get_architecture_info(),
        "Python Runtime": get_python_runtime_info(),
        "Container": container,
        "Container Storage": get_container_storage_info(container),
    }

if __name__ == "__main__":
    from pprint import pprint

    pprint(get_environment_diagnostics())
