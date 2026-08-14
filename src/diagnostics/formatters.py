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


def _first_storage_device(
    diagnostics: dict[str, Any],
) -> dict[str, Any]:
    """Return the first detected storage device, if available."""
    storage = (
        diagnostics
        .get("Hardware", {})
        .get("Storage", [])
    )

    if storage:
        return storage[0]

    return {}


def _first_gpu(
    diagnostics: dict[str, Any],
) -> dict[str, Any]:
    """Return the first detected GPU, if available."""
    gpus = (
        diagnostics
        .get("Hardware", {})
        .get("GPU", [])
    )

    if gpus:
        return gpus[0]

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

    storage = _first_storage_device(diagnostics)
    gpu = _first_gpu(diagnostics)

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

    gpu_name = gpu.get("Name", "GPU not detected")
    gpu_memory = gpu.get("Memory Total (MB)")

    if gpu_memory is not None:
        gpu_text = f"{gpu_name} | {gpu_memory / 1024:.1f} GB VRAM"
    else:
        gpu_text = gpu_name

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
        (
            f"Memory:    {ram_gb} GB RAM | "
            f"Storage: {storage_text}"
        ),
        f"OS:        {os_text}",
        (
            f"Runtime:   {python_implementation} "
            f"{python_version} | "
            f"{machine_architecture} | "
            f"{bitness.replace('bit', '-bit')}"
        ),
        f"AI Stack:  {ai_stack_text}",
    ]
    
    return "\n".join(lines)