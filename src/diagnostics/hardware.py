"""
Hardware diagnostics.

Collects relatively static information about the physical machine on which a workload is executing.

Initial implementation refactored from Iain Clark's MachineDiagnostics.ipynb notebook.

Currently supports:
    - Windows
    - Linux

Diagnostics include:
    - system manufacturer and model
    - CPU identity
    - physical and logical CPU counts
    - CPU clock frequency
    - installed RAM
    - RAM speed where available
    - physical storage devices
    - GPU identity where available
"""

from __future__ import annotations

import json
import platform
import re
import subprocess
from typing import Any

import psutil

try:
    import GPUtil
except ImportError:
    GPUtil = None


def _run_command(command: list[str]) -> str:
    """
    Run a system command and return stripped stdout.

    Returns an empty string if the command cannot be executed.
    """
    try:
        return subprocess.check_output(
            command,
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except Exception:
        return ""


def make_friendly_cpu_name(raw_name: str) -> str:
    """
    Convert a raw CPU description into a cleaner human-readable name.

    The raw CPU name is retained separately in the diagnostic record, so
    this function is intended for display rather than machine identification.
    """
    if not raw_name:
        return "Unknown CPU"

    name = re.sub(
        r"\(R\)|\(TM\)|CPU|@.*GHz",
        "",
        raw_name,
        flags=re.IGNORECASE,
    )
    name = re.sub(r"\s+", " ", name).strip()

    # Intel Core naming
    match = re.search(r"(i3|i5|i7|i9)-(\d{3,5})", name, re.IGNORECASE)

    if match:
        family, model_number = match.groups()
        model_number_int = int(model_number)

        if model_number_int < 1000:
            generation = "1st Gen"
        elif model_number_int < 10000:
            generation = f"{str(model_number_int)[0]}th Gen"
        else:
            generation = f"{str(model_number_int)[:2]}th Gen"

        return (
            f"Intel Core {family.lower()}-{model_number_int} "
            f"({generation})"
        )

    # Ryzen names are generally already readable.
    if "Ryzen" in name:
        return name

    return name


def get_system_model() -> dict[str, str]:
    """
    Return machine manufacturer and model where available.
    """
    system = platform.system()

    manufacturer = ""
    model = ""

    if system == "Windows":
        # PowerShell/CIM is preferred over WMIC.
        manufacturer = _run_command(
            [
                "powershell",
                "-Command",
                "(Get-CimInstance Win32_ComputerSystem).Manufacturer",
            ]
        )

        model = _run_command(
            [
                "powershell",
                "-Command",
                "(Get-CimInstance Win32_ComputerSystem).Model",
            ]
        )

        # WMIC fallback.
        if not manufacturer:
            output = _run_command(
                ["wmic", "computersystem", "get", "manufacturer"]
            )
            lines = [
                line.strip()
                for line in output.splitlines()
                if line.strip()
            ]
            if len(lines) > 1:
                manufacturer = lines[1]

        if not model:
            output = _run_command(
                ["wmic", "computersystem", "get", "model"]
            )
            lines = [
                line.strip()
                for line in output.splitlines()
                if line.strip()
            ]
            if len(lines) > 1:
                model = lines[1]

    elif system == "Linux":
        manufacturer = _run_command(
            ["cat", "/sys/devices/virtual/dmi/id/sys_vendor"]
        )

        model = _run_command(
            ["cat", "/sys/devices/virtual/dmi/id/product_name"]
        )

    return {
        "Manufacturer": manufacturer or "Unknown",
        "Model": model or "Unknown",
    }


def get_cpu_info() -> dict[str, Any]:
    """
    Return CPU identity, topology and clock information.
    """
    system = platform.system()
    raw_name = ""

    if system == "Windows":
        # PowerShell/CIM first.
        raw_name = _run_command(
            [
                "powershell",
                "-Command",
                "(Get-CimInstance Win32_Processor).Name",
            ]
        )

        # WMIC fallback.
        if not raw_name:
            output = _run_command(
                ["wmic", "cpu", "get", "Name"]
            )

            lines = [
                line.strip()
                for line in output.splitlines()
                if line.strip()
            ]

            if len(lines) > 1:
                raw_name = lines[1]

    elif system == "Linux":
        try:
            with open(
                "/proc/cpuinfo",
                encoding="utf-8",
            ) as cpuinfo:
                for line in cpuinfo:
                    if "model name" in line:
                        raw_name = line.split(":", 1)[1].strip()
                        break
        except Exception:
            pass

    # Generic fallback.
    if not raw_name:
        raw_name = platform.processor()

    frequency = psutil.cpu_freq()

    if frequency:
        clock_speed = {
            "Min (MHz)": round(frequency.min, 2),
            "Max (MHz)": round(frequency.max, 2),
            "Current (MHz)": round(frequency.current, 2),
        }
    else:
        clock_speed = None

    return {
        "CPU Name (Raw)": raw_name or "Unknown",
        "CPU Name (Friendly)": make_friendly_cpu_name(raw_name),
        "Cores (Physical)": psutil.cpu_count(logical=False),
        "Threads (Logical)": psutil.cpu_count(logical=True),
        "Clock Speed": clock_speed,
    }


def get_ram_info() -> dict[str, Any]:
    """
    Return installed RAM capacity and configured memory speed.

    Memory-speed detection is platform dependent and may require elevated
    privileges on Linux.
    """
    virtual_memory = psutil.virtual_memory()

    total_ram = virtual_memory.total

    ram_speed = None
    system = platform.system()

    if system == "Windows":
        output = _run_command(
            [
                "powershell",
                "-Command",
                (
                    "Get-CimInstance Win32_PhysicalMemory | "
                    "Select-Object -ExpandProperty Speed"
                ),
            ]
        )

        speeds = [
            int(value)
            for value in output.splitlines()
            if value.strip().isdigit()
        ]

        if speeds:
            ram_speed = sorted(set(speeds))

    elif system == "Linux":
        output = _run_command(
            ["dmidecode", "-t", "memory"]
        )

        speeds = re.findall(
            r"Configured Clock Speed: (\d+) MT/s",
            output,
        )

        if not speeds:
            speeds = re.findall(
                r"Speed: (\d+) MT/s",
                output,
            )

        if speeds:
            ram_speed = sorted(
                set(int(value) for value in speeds)
            )

    return {
        "Total RAM (Bytes)": total_ram,
        "Memory Speed": ram_speed,
    }


def get_storage_info() -> list[dict[str, Any]]:
    """
    Return information about physical storage devices.
    """
    system = platform.system()
    drives: list[dict[str, Any]] = []

    if system == "Windows":
        output = _run_command(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                r"""
                $result = Get-Disk | ForEach-Object {
                    $disk = $_

                    $volumes = @(
                        Get-Partition -DiskNumber $disk.Number -ErrorAction SilentlyContinue |
                        ForEach-Object {
                            $partition = $_
                            $volume = $partition |
                                Get-Volume -ErrorAction SilentlyContinue

                            [PSCustomObject]@{
                                PartitionNumber = $partition.PartitionNumber
                                DriveLetter     = if ($volume.DriveLetter) {
                                    "$($volume.DriveLetter):"
                                } else {
                                    $null
                                }
                                Label           = $volume.FileSystemLabel
                                FileSystem      = $volume.FileSystem
                                Size            = $partition.Size
                                MountPoint      = if ($volume.DriveLetter) {
                                    "$($volume.DriveLetter):\"
                                } else {
                                    $null
                                }
                            }
                        }
                    )

                    [PSCustomObject]@{
                        Number         = $disk.Number
                        Model          = $disk.FriendlyName
                        Manufacturer   = $disk.Manufacturer
                        Serial         = $disk.SerialNumber
                        Size           = $disk.Size
                        BusType        = "$($disk.BusType)"
                        LogicalVolumes = $volumes
                    }
                }

                $result | ConvertTo-Json -Depth 5 -Compress
                """,
            ]
        )

        if output:
            try:
                parsed = json.loads(output)

                if isinstance(parsed, dict):
                    parsed = [parsed]

                for disk in parsed:
                    logical_volumes = []

                    volumes = disk.get("LogicalVolumes") or []

                    if isinstance(volumes, dict):
                        volumes = [volumes]

                    for volume in volumes:
                        size = volume.get("Size")

                        logical_volumes.append(
                            {
                                "Partition": volume.get("PartitionNumber"),
                                "Drive": volume.get("DriveLetter"),
                                "Label": volume.get("Label"),
                                "File System": volume.get("FileSystem"),
                                "Size (Bytes)": (
                                    size if isinstance(size, (int, float)) else None
                                ),
                                "Mount Point": volume.get("MountPoint"),
                            }
                        )

                    size = disk.get("Size")

                    drives.append(
                        {
                            "Device": f"Disk {disk.get('Number')}",
                            "Model": disk.get("Model"),
                            "Manufacturer": disk.get("Manufacturer"),
                            "Serial": disk.get("Serial"),
                            "Size (Bytes)": (
                                size if isinstance(size, (int, float)) else None
                            ),
                            "BusType": disk.get("BusType"),
                            "Logical Volumes": logical_volumes,
                        }
                    )

            except (json.JSONDecodeError, TypeError, ValueError):
                pass
    elif system == "Linux":
        output = _run_command(
            [
                "lsblk",
                "-J",
                "-b",
                "-o",
                (
                    "NAME,TYPE,MODEL,VENDOR,SERIAL,SIZE,"
                    "TRAN,FSTYPE,LABEL,MOUNTPOINTS"
                ),
            ]
        )

        if output:
            try:
                parsed = json.loads(output)

                for disk in parsed.get("blockdevices", []):
                    if disk.get("type") != "disk":
                        continue

                    logical_volumes = []

                    for child in disk.get("children") or []:
                        child_type = child.get("type")

                        if child_type not in {
                            "part",
                            "lvm",
                            "crypt",
                            "raid",
                        }:
                            continue

                        size = child.get("size")
                        mount_points = child.get("mountpoints") or []

                        if isinstance(mount_points, str):
                            mount_points = [mount_points]

                        mount_point = next(
                            (
                                value
                                for value in mount_points
                                if value
                            ),
                            None,
                        )

                        logical_volumes.append(
                            {
                                "Partition": child.get("name"),
                                "Drive": None,
                                "Label": child.get("label"),
                                "File System": child.get("fstype"),
                                "Size (Bytes)": (
                                    size if isinstance(size, (int, float)) else None
                                ),
                                "Mount Point": mount_point,
                            }
                        )

                    size = disk.get("size")

                    drives.append(
                        {
                            "Device": f"/dev/{disk.get('name')}",
                            "Model": disk.get("model"),
                            "Manufacturer": disk.get("vendor"),
                            "Serial": disk.get("serial"),
                            "Size (Bytes)": (
                                size if isinstance(size, (int, float)) else None
                            ),
                            "BusType": disk.get("tran"),
                            "Logical Volumes": logical_volumes,
                        }
                    )

            except (
                json.JSONDecodeError,
                TypeError,
                ValueError,
            ):
                pass                

    return drives


def get_gpu_info():
    """
    Return GPU information and GPU detection status.

    GPUtil is treated as an optional dependency. Failure to import or execute
    GPUtil must not prevent the wider hardware diagnostic capture from
    completing.
    """

    if GPUtil is None:
        return {
            "Status": "Unavailable",
            "Detector": "GPUtil",
            "Reason": "Package not installed",
            "Devices": [],
        }

    try:
        gpus = GPUtil.getGPUs()
    except Exception as exc:
        return {
            "Status": "Failed",
            "Detector": "GPUtil",
            "Reason": str(exc),
            "Devices": [],
        }

    devices = [
        {
            "Name": gpu.name,
            "ID": gpu.id,
            "Memory Total (MB)": round(gpu.memoryTotal, 2),
        }
        for gpu in gpus
    ]

    return {
        "Status": "Detected" if devices else "Not detected",
        "Detector": "GPUtil",
        "Reason": None,
        "Devices": devices,
    }

def get_hardware_diagnostics() -> dict[str, Any]:
    """
    Capture a complete static hardware diagnostic snapshot.
    """
    return {
        "System": get_system_model(),
        "CPU": get_cpu_info(),
        "RAM": get_ram_info(),
        "Storage": get_storage_info(),
        "GPU": get_gpu_info(),
    }


if __name__ == "__main__":
    from pprint import pprint

    pprint(get_hardware_diagnostics())