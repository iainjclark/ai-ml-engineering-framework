"""Shell utilities."""

from __future__ import annotations

import subprocess


def _run_command(command: list[str], timeout: float = 10.0) -> str:
    """
    Run a system command and return stripped stdout.

    Returns an empty string if the command cannot be executed, exits
    non-zero, or does not complete within the timeout. Programming errors
    are deliberately not caught: a bare `except Exception` here would mask
    them as an absent tool across every platform probe.
    """
    try:
        return subprocess.check_output(
            command,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=timeout,
        ).strip()
    except (OSError, subprocess.SubprocessError):
        return ""
