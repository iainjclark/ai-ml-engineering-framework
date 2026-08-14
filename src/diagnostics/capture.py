"""
Unified diagnostic capture.

Aggregates hardware, environment, and runtime diagnostics into a single
structured record suitable for logging, persistence, or inclusion in
engineering evidence.

This module does not perform detailed diagnostics itself. It coordinates
the lower-level diagnostic modules.

Current diagnostic domains:
    - hardware
    - environment
    - runtime
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .environment import get_environment_diagnostics
from .hardware import get_hardware_diagnostics
from .runtime import get_runtime_diagnostics


def capture_diagnostics() -> dict[str, Any]:
    """
    Capture a unified diagnostic snapshot.

    Returns
    -------
    dict
        Structured diagnostic information including capture timestamp,
        hardware configuration, execution environment, and current runtime
        resource state.
    """
    captured_at = datetime.now(timezone.utc)

    return {
        "Captured At (UTC)": captured_at.isoformat(),
        "Hardware": get_hardware_diagnostics(),
        "Environment": get_environment_diagnostics(),
        "Runtime": get_runtime_diagnostics(),
    }


if __name__ == "__main__":
    from pprint import pprint

    pprint(capture_diagnostics())
