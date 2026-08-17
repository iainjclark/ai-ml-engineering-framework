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
import socket
from typing import Any

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
    """
    Capture a structured execution-environment diagnostic snapshot.
    """
    return {
        "Host": get_host_info(),
        "Operating System": get_os_info(),
        "Architecture": get_architecture_info(),
        "Python Runtime": get_python_runtime_info(),
    }


if __name__ == "__main__":
    from pprint import pprint

    pprint(get_environment_diagnostics())