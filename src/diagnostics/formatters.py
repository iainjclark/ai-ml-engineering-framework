"""
Diagnostic output formatters.

The formatter provides human-readable representations of diagnostic capture records.

    formatters.py
        Presents selected information for human consumption.

The formatter is intentionally separate from capture.py which preserves as much of the full 
state of the system as it can

    capture.py
        Captures the complete engineering diagnostic record.

"""

from __future__ import annotations

from .software import get_packages_in_category

from typing import Any

def _format_size(size_bytes: int | float | None) -> str | None:
    """Format a byte count using an appropriate human-readable unit."""
    if not isinstance(size_bytes, (int, float)):
        return None

    size = max(0, size_bytes)

    units = (
        ("TB", 1000**4),
        ("GB", 1000**3),
        ("MB", 1000**2),
        ("KB", 1000),
        ("B", 1),
    )

    for unit, divisor in units:
        if size >= divisor or unit == "B":
            value = size / divisor

            if unit in {"TB", "GB"} and value < 10:
                return f"{value:.1f} {unit}"

            return f"{value:.0f} {unit}"

    return "0 B"
    
def _storage_devices(
    diagnostics: dict[str, Any],
) -> list[dict[str, Any]]:
    """Return all detected storage devices."""
    storage = (
        diagnostics
        .get("Hardware", {})
        .get("Storage", [])
    )

    return storage if isinstance(storage, list) else []

def _format_logical_volume(volume: dict[str, Any]) -> str:
    """Return a concise description of a mounted logical volume."""
    parts = []

    drive = volume.get("Drive")
    mount_point = volume.get("Mount Point")
    label = volume.get("Label")
    size = volume.get("Size (Bytes)")
    file_system = volume.get("File System")

    identifier = drive or mount_point

    if identifier:
        parts.append(str(identifier))

    if label:
        parts.append(str(label))

    size_text = _format_size(size)
    if size_text:
        parts.append(size_text)

    if file_system:
        parts.append(str(file_system))

    return " | ".join(parts)

def _first_gpu(
    diagnostics: dict[str, Any],
) -> dict[str, Any]:
    """Return the first detected GPU device, if available."""
    gpu_info = (
        diagnostics
        .get("Hardware", {})
        .get("GPU", {})
    )

    devices = gpu_info.get("Devices", [])

    if devices:
        return devices[0]

    return {}

def format_diagnostics(
    diagnostics: dict[str, Any],
    style: str = "concise",
) -> str:
    """
    Format a diagnostic capture for human-readable display.

    Parameters
    ----------
    diagnostics:
        Diagnostic record returned by capture_diagnostics().

    style:
        Output style.

        Currently supported:
            "concise"

    Returns
    -------
    str
        Human-readable diagnostic summary.
    """
    if style == "concise":
        return _format_concise(diagnostics)

    raise ValueError(
        f"Unsupported diagnostic format style: {style!r}"
    )


def _format_concise(
    diagnostics: dict[str, Any],
) -> str:
    """
    Return a compact diagnostic summary.

    Intended for README files, console output, model cards and other
    contexts where a full diagnostic record would be unnecessarily verbose.
    """
    hardware = diagnostics.get("Hardware", {})
    environment = diagnostics.get("Environment", {})
    container = environment.get("Container", {})
    container_storage = environment.get("Container Storage")

    system = hardware.get("System", {})
    cpu = hardware.get("CPU", {})
    ram = hardware.get("RAM", {})

    operating_system = environment.get(
        "Operating System",
        {},
    )

    architecture = environment.get(
        "Architecture",
        {},
    )

    python_runtime = environment.get(
        "Python Runtime",
        {},
    )

    storage_devices = _storage_devices(diagnostics)

    manufacturer = system.get("Manufacturer", "Unknown")
    model = system.get("Model", "Unknown")

    system_parts = [
        value
        for value in (manufacturer, model)
        if value and value != "Unknown"
    ]

    system_text = (
        " ".join(system_parts)
        if system_parts
        else "System information not detected"
    )

    os_name = operating_system.get("System", "Unknown")
    os_release = operating_system.get("Release", "Unknown")

    if os_name == "Linux":
        os_text = operating_system.get(
            "Distribution",
            "Linux",
        )
        kernel_text = f"Linux {os_release}"
    else:
        os_version = operating_system.get("Version")

        if os_version:
            os_text = f"{os_name} {os_release} ({os_version})"
        else:
            os_text = f"{os_name} {os_release}"

        kernel_text = None

    cpu_name = (
        cpu.get("CPU Name (Friendly)")
        or cpu.get("CPU Name (Raw)")
        or "Unknown CPU"
    )

    physical_cores = cpu.get("Cores (Physical)", "?")
    logical_threads = cpu.get("Threads (Logical)", "?")

    ram_gb = ram.get("Total RAM (GB)", "?")

    gpu_info = hardware.get("GPU", {})
    gpu_devices = gpu_info.get("Devices", [])
    gpu_status = gpu_info.get("Status", "Unknown")

    if gpu_devices:
        gpu = gpu_devices[0]

        gpu_name = gpu.get("Name", "Unknown GPU")
        gpu_memory = gpu.get("Memory Total (MB)")

        if gpu_memory is not None:
            gpu_text = (
                f"{gpu_name} | "
                f"{gpu_memory / 1024:.1f} GB VRAM"
            )
        else:
            gpu_text = gpu_name

    elif gpu_status == "Unavailable":
        gpu_text = (
            "GPU detection unavailable "
            "(GPUtil not installed; install with pip or conda)"
        )

    elif gpu_status == "Failed":
        gpu_text = "GPU detection failed"

    else:
        gpu_text = "GPU not detected"

    storage_lines = []

    # In a container, prefer the filesystem/storage actually visible to
    # the running workload rather than virtual block devices exposed by
    # the container runtime.
    if container.get("Detected") and container_storage:
        storage_parts = ["container"]

        mount_point = container_storage.get("Mount Point", "/")
        size = container_storage.get("Size (Bytes)")
        available = container_storage.get("Available (Bytes)")
        file_system = container_storage.get("File System")

        if mount_point:
            storage_parts.append(str(mount_point))

        size_text = _format_size(size)
        if size_text:
            storage_parts.append(f"{size_text} total")

        available_text = _format_size(available)
        if available_text:
            storage_parts.append(f"{available_text} free")

        if file_system:
            storage_parts.append(str(file_system))

        storage_lines.append(
            "Storage:   " + " | ".join(storage_parts)
        )

    else:
        # Bare-metal / host-visible physical storage.
        for storage_index, storage in enumerate(storage_devices):
            storage_model = (
                storage.get("Model")
                or "Unknown storage"
            )

            storage_size = storage.get("Size (Bytes)")
            storage_bus = storage.get("BusType")

            storage_parts = [str(storage_model)]

            storage_size_text = _format_size(storage_size)
            if storage_size_text:
                storage_parts.append(storage_size_text)

            if storage_bus:
                storage_parts.append(str(storage_bus))

            storage_text = " | ".join(storage_parts)

            # Only mounted/addressable logical volumes belong
            # in concise output.
            logical_volumes = [
                volume
                for volume in storage.get("Logical Volumes", [])
                if volume.get("Drive") or volume.get("Mount Point")
            ]

            prefix = (
                "Storage:   "
                if storage_index == 0
                else "           "
            )

            if len(logical_volumes) == 1:
                volume_text = _format_logical_volume(
                    logical_volumes[0]
                )

                storage_lines.append(
                    f"{prefix}{storage_text} | {volume_text}"
                )

            elif len(logical_volumes) > 1:
                # Physical device
                storage_lines.append(
                    f"{prefix}{storage_text}"
                )

                # Logical volumes belonging to that device
                for volume in logical_volumes:
                    volume_text = _format_logical_volume(volume)

                    storage_lines.append(
                        f"             {volume_text}"
                    )

            else:
                storage_lines.append(
                    f"{prefix}{storage_text}"
                )

        if not storage_lines:
            storage_lines.append(
                "Storage:   Storage not detected"
            )

    python_version = python_runtime.get(
        "Version",
        "Unknown",
    )

    python_implementation = python_runtime.get(
        "Implementation",
        "Python",
    )

    machine_architecture = architecture.get(
        "Machine",
        "Unknown",
    )

    bitness = architecture.get(
        "Architecture",
        "Unknown",
    )

    software = diagnostics.get("Software", {})
    packages = software.get("Packages", {})

    def _stack_text(category: str, absent: str) -> str:
        """Render one category of tracked packages as a summary line."""
        detected = [
            f"{name} {packages[name]}"
            for name in get_packages_in_category(category)
            if packages.get(name)
        ]

        return " | ".join(detected) if detected else absent

    numerics_text = _stack_text(
        "numerics",
        "No tracked numerical packages detected",
    )

    ai_stack_text = _stack_text(
        "ml",
        "No tracked AI/ML packages detected",
    )

    core_label = "core" if physical_cores == 1 else "cores"
    thread_label = "thread" if logical_threads == 1 else "threads"

    lines = [
        f"System:    {system_text}",
    ]

    if container.get("Detected"):
        container_type = container.get("Type") or "Container"
        lines.append(
            f"Container: {container_type}"
        )

    lines.extend([
        (
            f"Compute:   {cpu_name} | "
            f"{physical_cores} {core_label} / "
            f"{logical_threads} {thread_label} | "
            f"{gpu_text}"
        ),
        f"Memory:    {ram_gb} GB RAM",
    ])

    lines.extend(storage_lines)

    lines.append(f"OS:        {os_text}")

    if kernel_text:
        lines.append(f"Kernel:    {kernel_text}")

    lines.extend([
        (
            f"Runtime:   {python_implementation} "
            f"{python_version} | "
            f"{machine_architecture} | "
            f"{bitness.replace('bit', '-bit')}"
        ),
        f"Numerics:  {numerics_text}",
        f"AI Stack:  {ai_stack_text}",
    ])

    return "\n".join(lines)