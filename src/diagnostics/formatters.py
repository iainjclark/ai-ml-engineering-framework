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

from typing import Any

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
    size = volume.get("Size (GB)")
    file_system = volume.get("File System")

    identifier = drive or mount_point

    if identifier:
        parts.append(str(identifier))

    if label:
        parts.append(str(label))

    if size is not None:
        if isinstance(size, (int, float)):
            parts.append(f"{size:.0f} GB")
        else:
            parts.append(str(size))

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
    Return a compact five-line diagnostic summary.

    Intended for README files, console output, model cards and other
    contexts where a full diagnostic record would be unnecessarily verbose.
    """
    hardware = diagnostics.get("Hardware", {})
    environment = diagnostics.get("Environment", {})

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

    os_name = operating_system.get("System", "Unknown")
    os_release = operating_system.get("Release", "Unknown")
    os_version = operating_system.get("Version")

    if os_version:
        os_text = f"{os_name} {os_release} ({os_version})"
    else:
        os_text = f"{os_name} {os_release}"

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

    for storage_index, storage in enumerate(storage_devices):
        storage_model = storage.get("Model", "Unknown storage")

        storage_size = (
            storage.get("Size (GB)")
            or storage.get("Size")
        )

        storage_bus = storage.get("BusType")

        storage_parts = [str(storage_model)]

        if storage_size is not None:
            if isinstance(storage_size, (int, float)):
                storage_parts.append(f"{storage_size:.0f} GB")
            else:
                storage_parts.append(str(storage_size))

        if storage_bus:
            storage_parts.append(str(storage_bus))

        storage_text = " | ".join(storage_parts)

        # Only mounted/addressable logical volumes belong in concise output.
        logical_volumes = [
            volume
            for volume in storage.get("Logical Volumes", [])
            if volume.get("Drive") or volume.get("Mount Point")
        ]
        
        prefix = "Storage:   " if storage_index == 0 else "           "
        
        if len(logical_volumes) == 1:
            volume_text = _format_logical_volume(logical_volumes[0])

            storage_lines.append(
                f"{prefix}{storage_text} | {volume_text}"
            )

        elif len(logical_volumes) > 1:
            storage_lines.append(
                f"Storage:   {storage_text}"
            )

            for volume in logical_volumes:
                volume_text = _format_logical_volume(volume)

                storage_lines.append(
                    f"             {volume_text}"
                )

        else:
            storage_lines.append(
                f"Storage:   {storage_text}"
            )

    if not storage_lines:
        storage_lines.append("Storage:   Storage not detected")
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

    ai_packages = []

    for name in ("scikit-learn", "PyTorch", "TensorFlow"):
        version = packages.get(name)

        if version:
            ai_packages.append(f"{name} {version}")

    ai_stack_text = (
        " | ".join(ai_packages)
        if ai_packages
        else "No tracked AI/ML packages detected"
    )
    lines = [
        f"System:    {manufacturer} {model}",
        (
            f"Compute:   {cpu_name} | "
            f"{physical_cores} cores / "
            f"{logical_threads} threads | "
            f"{gpu_text}"
        ),
        f"Memory:    {ram_gb} GB RAM",
    ]

    lines.extend(storage_lines)

    lines.extend([
        f"OS:        {os_text}",
        (
            f"Runtime:   {python_implementation} "
            f"{python_version} | "
            f"{machine_architecture} | "
            f"{bitness.replace('bit', '-bit')}"
        ),
        f"AI Stack:  {ai_stack_text}",
    ])
    
    return "\n".join(lines)