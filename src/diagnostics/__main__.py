"""Command-line entry point for system diagnostics."""

from .capture import capture_diagnostics
from .formatters import format_diagnostics


def main() -> None:
    """Capture and print a concise diagnostic summary."""
    diagnostics = capture_diagnostics()
    print(format_diagnostics(diagnostics))


if __name__ == "__main__":
    main()
