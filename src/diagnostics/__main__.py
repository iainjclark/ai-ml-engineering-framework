"""Command-line entry point for system diagnostics."""

from .capture import capture_diagnostics
from .formatters import format_diagnostics

import sys

_STATUS_MESSAGE = "Running... (might take 10-15s)"

def _show_status() -> bool:
    """Show the temporary progress message on an interactive terminal."""
    if not sys.stdout.isatty():
        return False

    sys.stdout.write(_STATUS_MESSAGE)
    sys.stdout.flush()

    return True


def _clear_status() -> None:
    """Erase the temporary progress message from the terminal."""
    width = len(_STATUS_MESSAGE)

    # Move back over the message, overwrite it with spaces,
    # then return to the original cursor position.
    sys.stdout.write(
        "\b" * width
        + " " * width
        + "\b" * width
    )
    sys.stdout.flush()


def main() -> None:
    """Capture and print a concise diagnostic summary."""
    status_visible = _show_status()

    diagnostics = capture_diagnostics()
    output = format_diagnostics(diagnostics)

    if status_visible:
        _clear_status()

    print(output)


if __name__ == "__main__":
    main()
    