"""
Software stack diagnostics.

Captures versions of key scientific-computing and AI/ML packages available
to the current Python execution environment.

Versions are obtained from the imported runtime modules where possible,
so the diagnostic record reflects the software actually visible to the
executing Python interpreter.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from typing import Any, Optional

# Display name -> Python import name
DEFAULT_PACKAGES = {
    "NumPy": "numpy",
    "SciPy": "scipy",
    "pandas": "pandas",
    "scikit-learn": "scikit-learn",
    "PyTorch": "torch",
    "TensorFlow": "tensorflow",
}

def get_package_version(package_name: str) -> Optional[str]:
    """
    Return the installed version of a package without importing it.

    This avoids import-time side effects from heavyweight packages such as
    TensorFlow and PyTorch.
    """
    try:
        return version(package_name)
    except PackageNotFoundError:
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
