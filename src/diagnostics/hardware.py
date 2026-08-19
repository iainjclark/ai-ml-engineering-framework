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

from ._shell import _run_command

try:
    import GPUtil
except ImportError:
    GPUtil = None

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
    elif system == "Darwin":
        output = _run_command(
            [
                "system_profiler",
                "SPHardwareDataType",
            ]
        )

        model_name = ""
        model_identifier = ""

        for line in output.splitlines():
            line = line.strip()

            if line.startswith("Model Name:"):
                model_name = line.split(":", 1)[1].strip()

            elif line.startswith("Model Identifier:"):
                model_identifier = line.split(":", 1)[1].strip()

        manufacturer = "Apple"

        if model_name and model_identifier:
            model = f"{model_name} ({model_identifier})"
        else:
            model = model_name or model_identifier

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
    elif system == "Darwin":
        machine = platform.machine()

        if machine == "arm64":
            output = _run_command(
                [
                    "system_profiler",
                    "SPHardwareDataType",
                ]
            )

            for line in output.splitlines():
                line = line.strip()

                if line.startswith("Chip:"):
                    raw_name = line.split(":", 1)[1].strip()
                    break

        else:
            raw_name = _run_command(
                [
                    "sysctl",
                    "-n",
                    "machdep.cpu.brand_string",
                ]
            )


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

def _get_macos_storage_info() -> list[dict[str, Any]]:
    """
    Return macOS physical storage devices and their logical volumes.

    Handles:
        - the macOS startup disk
        - additional internal disks
        - USB flash drives
        - external SSDs/HDDs
        - mounted and unmounted partitions
        - APFS synthesized containers and volumes

    Uses diskutil plist output rather than scraping human-readable text.
    """

    import plistlib

    drives: list[dict[str, Any]] = []

    def _diskutil_plist(
        command: list[str],
    ) -> dict[str, Any] | None:
        """
        Run diskutil and parse its plist output.
        """
        try:
            output = subprocess.check_output(
                [
                    "/usr/sbin/diskutil",
                    *command,
                ],
                stderr=subprocess.DEVNULL,
            )

            return plistlib.loads(output)

        except (
            OSError,
            subprocess.CalledProcessError,
            plistlib.InvalidFileException,
            ValueError,
        ):
            return None

    def _diskutil_info(
        target: str,
    ) -> dict[str, Any] | None:
        """
        Return diskutil plist information for a disk, partition,
        volume or mount point.
        """
        return _diskutil_plist(
            [
                "info",
                "-plist",
                target,
            ]
        )

    def _whole_disk_from_identifier(
        identifier: str,
    ) -> str | None:
        """
        Resolve a partition/device identifier to its whole disk.

        Examples:
            disk0      -> disk0
            disk0s2    -> disk0
            disk4s1    -> disk4
        """

        info = _diskutil_info(identifier)

        if info:
            if info.get("Whole"):
                return identifier

            parent = (
                info.get("ParentWholeDisk")
                or info.get("PartOfWhole")
            )

            if isinstance(parent, str) and parent:
                return parent

        # Safe fallback for conventional macOS disk identifiers.
        match = re.match(r"^(disk\d+)", identifier)

        if match:
            return match.group(1)

        return None

    def _make_logical_volume(
        entry: dict[str, Any],
    ) -> dict[str, Any] | None:
        """
        Convert a diskutil partition/APFS-volume record into the
        common logical-volume schema.
        """

        identifier = entry.get("DeviceIdentifier")

        if not identifier:
            return None

        # diskutil list contains useful information, but diskutil info
        # generally gives us better filesystem and mount-point metadata.
        info = _diskutil_info(identifier) or {}

        size = (
            info.get("TotalSize")
            or entry.get("Size")
        )

        if not isinstance(size, (int, float)):
            size = None

        return {
            "Partition": identifier,
            "Drive": None,
            "Label": (
                info.get("VolumeName")
                or entry.get("VolumeName")
                or entry.get("Name")
            ),
            "File System": (
                info.get("FilesystemType")
                or info.get("FilesystemName")
                or entry.get("FilesystemType")
                or entry.get("Content")
            ),
            "Size (Bytes)": size,
            "Mount Point": (
                info.get("MountPoint")
                or entry.get("MountPoint")
            ),
        }

    def _physical_drive_record(
        identifier: str,
        fallback_entry: dict[str, Any] | None = None,
    ) -> dict[str, Any] | None:
        """
        Build the common physical-drive schema for one whole disk.
        """

        disk_info = _diskutil_info(identifier)

        if not disk_info:
            return None

        # diskutil can expose synthesized APFS containers and disk images
        # as whole disks. They are not physical storage devices.
        virtual_or_physical = disk_info.get("VirtualOrPhysical")

        if (
            isinstance(virtual_or_physical, str)
            and virtual_or_physical.lower() == "virtual"
        ):
            return None

        if disk_info.get("Whole") is False:
            return None

        size = disk_info.get("TotalSize")

        if (
            not isinstance(size, (int, float))
            and fallback_entry
        ):
            size = fallback_entry.get("Size")

        if not isinstance(size, (int, float)):
            size = None

        return {
            "Device": identifier,
            "Model": (
                disk_info.get("MediaName")
                or disk_info.get("DeviceModel")
                or (
                    fallback_entry.get("VolumeName")
                    if fallback_entry
                    else None
                )
                or identifier
            ),
            "Manufacturer": (
                disk_info.get("DeviceVendor")
                or disk_info.get("MediaType")
            ),
            "Serial": (
                disk_info.get("SerialNumber")
                or disk_info.get("DiskUUID")
            ),
            "Size (Bytes)": size,
            "BusType": (
                disk_info.get("BusProtocol")
                or disk_info.get("Protocol")
            ),
            "Logical Volumes": [],
        }

    def _add_logical_volume(
        drive: dict[str, Any],
        volume: dict[str, Any],
    ) -> None:
        """
        Add a logical volume to a physical drive without duplicates.
        """

        identifier = volume.get("Partition")

        existing_identifiers = {
            item.get("Partition")
            for item in drive.get("Logical Volumes", [])
        }

        if identifier not in existing_identifiers:
            drive["Logical Volumes"].append(volume)

    # ------------------------------------------------------------------
    # Obtain the complete macOS disk topology.
    #
    # This intentionally does NOT use:
    #
    #     diskutil list -plist physical
    #
    # because we need both the physical disks and synthesized APFS
    # containers in order to map APFS volumes back to their stores.
    # ------------------------------------------------------------------

    disk_list = _diskutil_plist(
        [
            "list",
            "-plist",
        ]
    )

    # If full enumeration fails, still try to identify the physical
    # disk backing the startup filesystem.
    if not disk_list:
        root_info = _diskutil_info("/")

        if not root_info:
            return drives

        physical_stores = (
            root_info.get("APFSPhysicalStores")
            or []
        )

        for store in physical_stores:
            store_identifier = (
                store.get("APFSPhysicalStore")
                or store.get("DeviceIdentifier")
            )

            if not store_identifier:
                continue

            whole_disk = _whole_disk_from_identifier(
                store_identifier
            )

            if not whole_disk:
                continue

            drive = _physical_drive_record(
                whole_disk
            )

            if not drive:
                continue

            root_volume = {
                "Partition": root_info.get(
                    "DeviceIdentifier"
                ),
                "Drive": None,
                "Label": root_info.get("VolumeName"),
                "File System": (
                    root_info.get("FilesystemType")
                    or root_info.get("FilesystemName")
                    or root_info.get("Content")
                ),
                "Size (Bytes)": (
                    root_info.get("APFSContainerSize")
                    or root_info.get("TotalSize")
                ),
                "Mount Point": root_info.get("MountPoint"),
            }

            drive["Logical Volumes"].append(
                root_volume
            )

            drives.append(drive)

        return drives

    disk_entries = disk_list.get(
        "AllDisksAndPartitions",
        [],
    )

    # Index every top-level diskutil entry by device identifier.
    entries_by_identifier = {
        entry.get("DeviceIdentifier"): entry
        for entry in disk_entries
        if entry.get("DeviceIdentifier")
    }

    # ------------------------------------------------------------------
    # Discover actual physical whole disks.
    # ------------------------------------------------------------------

    physical_drives: dict[str, dict[str, Any]] = {}

    candidate_whole_disks = (
        disk_list.get("WholeDisks")
        or []
    )

    for identifier in candidate_whole_disks:
        entry = entries_by_identifier.get(identifier)

        drive = _physical_drive_record(
            identifier,
            entry,
        )

        if drive:
            physical_drives[identifier] = drive

    # Some diskutil versions/configurations may provide incomplete
    # WholeDisks metadata, so inspect top-level partitioned devices too.
    for entry in disk_entries:
        identifier = entry.get("DeviceIdentifier")

        if not identifier:
            continue

        if identifier in physical_drives:
            continue

        # Physical partitioned disks normally have a Partitions array.
        # Synthesized APFS containers normally have APFSVolumes instead.
        if not entry.get("Partitions"):
            continue

        drive = _physical_drive_record(
            identifier,
            entry,
        )

        if drive:
            physical_drives[identifier] = drive

    # ------------------------------------------------------------------
    # Map ordinary partitions directly onto their physical disks.
    # ------------------------------------------------------------------

    for disk_identifier, drive in physical_drives.items():
        disk_entry = entries_by_identifier.get(
            disk_identifier,
            {},
        )

        for partition in (
            disk_entry.get("Partitions")
            or []
        ):
            partition_identifier = partition.get(
                "DeviceIdentifier"
            )

            if not partition_identifier:
                continue

            # An Apple_APFS partition is a physical store. Its actual
            # user-visible volumes are represented by the synthesized
            # APFS container and are added below.
            content = str(
                partition.get("Content") or ""
            )

            if content.startswith("Apple_APFS"):
                continue

            volume = _make_logical_volume(
                partition
            )

            if volume:
                _add_logical_volume(
                    drive,
                    volume,
                )

    # ------------------------------------------------------------------
    # Map synthesized APFS containers back to their physical stores.
    # ------------------------------------------------------------------

    for container_entry in disk_entries:
        apfs_volumes = (
            container_entry.get("APFSVolumes")
            or []
        )

        physical_stores = (
            container_entry.get("APFSPhysicalStores")
            or []
        )

        # If this is not an APFS container, there is nothing to map.
        if not apfs_volumes and not physical_stores:
            continue

        container_identifier = container_entry.get(
            "DeviceIdentifier"
        )

        # Some macOS versions expose additional APFS topology through
        # `diskutil info`, so use it as a fallback/enrichment source.
        container_info = (
            _diskutil_info(container_identifier)
            if container_identifier
            else None
        ) or {}

        if not physical_stores:
            physical_stores = (
                container_info.get(
                    "APFSPhysicalStores"
                )
                or []
            )

        if not apfs_volumes:
            apfs_volumes = (
                container_info.get(
                    "APFSVolumes"
                )
                or []
            )

        backing_disks: set[str] = set()

        for store in physical_stores:
            store_identifier = (
                store.get("DeviceIdentifier")
                or store.get("APFSPhysicalStore")
            )

            if not store_identifier:
                continue

            whole_disk = _whole_disk_from_identifier(
                store_identifier
            )

            if whole_disk:
                backing_disks.add(whole_disk)

        if not backing_disks:
            continue

        for apfs_volume_entry in apfs_volumes:
            volume = _make_logical_volume(
                apfs_volume_entry
            )

            if not volume:
                continue

            for backing_disk in backing_disks:
                drive = physical_drives.get(
                    backing_disk
                )

                if drive:
                    _add_logical_volume(
                        drive,
                        volume,
                    )

    # ------------------------------------------------------------------
    # Ensure the currently mounted root filesystem is represented.
    #
    # Modern macOS normally boots from an APFS snapshot, so "/" may not
    # correspond directly to one of the APFS volume records returned by
    # `diskutil list`.
    # ------------------------------------------------------------------

    root_info = _diskutil_info("/")

    system_disks: set[str] = set()

    if root_info:
        physical_stores = (
            root_info.get("APFSPhysicalStores")
            or []
        )

        for store in physical_stores:
            store_identifier = (
                store.get("APFSPhysicalStore")
                or store.get("DeviceIdentifier")
            )

            if not store_identifier:
                continue

            whole_disk = _whole_disk_from_identifier(
                store_identifier
            )

            if not whole_disk:
                continue

            system_disks.add(whole_disk)

            drive = physical_drives.get(
                whole_disk
            )

            if not drive:
                drive = _physical_drive_record(
                    whole_disk
                )

                if drive:
                    physical_drives[
                        whole_disk
                    ] = drive

            if not drive:
                continue

            root_volume = {
                "Partition": root_info.get(
                    "DeviceIdentifier"
                ),
                "Drive": None,
                "Label": root_info.get("VolumeName"),
                "File System": (
                    root_info.get("FilesystemType")
                    or root_info.get("FilesystemName")
                    or root_info.get("Content")
                ),
                "Size (Bytes)": (
                    root_info.get("APFSContainerSize")
                    or root_info.get("TotalSize")
                ),
                "Mount Point": root_info.get("MountPoint"),
            }

            _add_logical_volume(
                drive,
                root_volume,
            )

    # ------------------------------------------------------------------
    # Stable presentation order:
    #
    #   1. system disk(s)
    #   2. other internal disks
    #   3. external/removable disks
    # ------------------------------------------------------------------

    def _drive_sort_key(
        item: tuple[str, dict[str, Any]],
    ) -> tuple[int, int, str]:
        identifier, _drive = item

        info = _diskutil_info(identifier) or {}

        is_system = identifier in system_disks
        is_internal = bool(
            info.get("Internal")
        )

        return (
            0 if is_system else 1,
            0 if is_internal else 1,
            identifier,
        )

    for _, drive in sorted(
        physical_drives.items(),
        key=_drive_sort_key,
    ):
        drives.append(drive)

    return drives

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

    elif system == "Darwin":
        drives.extend(_get_macos_storage_info())

    return drives

def get_gpu_info():
    """
    Return GPU information and GPU detection status.

    GPUtil is treated as an optional dependency. Failure to import or execute
    GPUtil must not prevent the wider hardware diagnostic capture from
    completing. However, for macOS we can use system_profiler SPDisplaysDataType
    """
    system = platform.system()

    if system == "Darwin":
        output = _run_command(
            [
                "system_profiler",
                "SPDisplaysDataType",
            ]
        )

        devices = []
        current_device = {}

        for line in output.splitlines():
            stripped = line.strip()

            if stripped.startswith("Chipset Model:"):
                if current_device:
                    devices.append(current_device)

                gpu_name = stripped.split(":", 1)[1].strip()

                if gpu_name.startswith("Apple ") and not gpu_name.endswith(" GPU"):
                    gpu_name = f"{gpu_name} GPU"

                current_device = {
                    "Name": gpu_name,
                    "ID": None,
                    "Memory Total (MB)": None,
                }

            elif stripped.startswith("VRAM") and current_device:
                # Mainly useful for older Intel/discrete-GPU Macs.
                value = stripped.split(":", 1)[1].strip()
                current_device["VRAM Description"] = value

        if current_device:
            devices.append(current_device)

        return {
            "Status": "Detected" if devices else "Not detected",
            "Detector": "system_profiler",
            "Reason": None,
            "Devices": devices,
        }

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
