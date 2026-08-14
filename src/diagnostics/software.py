"""
Software stack diagnostics.

Captures versions of key scientific-computing and AI/ML packages available
to the current Python execution environment.

Versions are obtained from the imported runtime modules where possible,
so the diagnostic record reflects the software actually visible to the
executing Python interpreter.
"""

from __future__ import annotations

import importlib
from typing import Any


# Display name -> Python import name
DEFAULT_PACKAGES = {
    "NumPy": "numpy",
    "SciPy": "scipy",
    "pandas": "pandas",
    "scikit-learn": "sklearn",
    "PyTorch": "torch",
    "TensorFlow": "tensorflow",
}


def get_package_version(
    module_name: str,
) -> str | None:
    """
    Return the version reported by an importable Python module.

    Returns None if the module cannot be imported or does not expose
    a __version__ attribute.
    """
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, "__version__", None)
        return str(version) if version is not None else None

    except Exception:
        return None

def get_package_versions(
    packages: dict[str, str] | None = None,
) -> dict[str, str | None]:
    """
    Return versions of selected Python packages.

    Packages that are unavailable in the current execution environment
    are represented by None.
    """
    packages = packages or DEFAULT_PACKAGES

    return {
        display_name: get_package_version(module_name)
        for display_name, module_name in packages.items()
    }


def get_software_diagnostics() -> dict[str, Any]:
    """
    Capture a structured software-stack diagnostic snapshot.
    """
    return {
        "Packages": get_package_versions(),
    }


if __name__ == "__main__":
    from pprint import pprint

    pprint(get_software_diagnostics())
