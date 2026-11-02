"""Command-line entry point for system diagnostics."""

from .capture import capture_diagnostics
from .formatters import format_diagnostics

import argparse
import json
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
    """Capture diagnostics as a concise summary or JSON."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the full diagnostic record as JSON.",
    )
    args = parser.parse_args()

    status_visible = False
    if not args.json:
        status_visible = _show_status()

    try:
        diagnostics = capture_diagnostics()
        output = (
            json.dumps(diagnostics, indent=2)
            if args.json
            else format_diagnostics(diagnostics)
        )
    finally:
        if status_visible:
            _clear_status()

    print(output)


if __name__ == "__main__":
    main()
    