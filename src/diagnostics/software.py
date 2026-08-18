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
from typing import Any

# Display name -> (distribution name, category).
#
# The value is the *distribution* name passed to importlib.metadata.version(),
# which is not always the import name (scikit-learn imports as `sklearn`).
#
# The category is what the formatter filters on. It lives here rather than in
# formatters.py so that adding a package registers it for both capture and
# display in one edit; a second hardcoded list in the formatter can silently
# drift out of step with this one.
#
#   numerics - numerical computing and dataframe libraries. Not modelling
#              frameworks, but among the most reproducibility-relevant facts
#              in the record: NumPy ABI breaks and the pandas 3.0 copy-on-write
#              default both change results from unchanged code.
#   ml       - modelling frameworks, classical and deep learning.
DEFAULT_PACKAGES = {
    "NumPy": ("numpy", "numerics"),
    "SciPy": ("scipy", "numerics"),
    "pandas": ("pandas", "numerics"),
    "scikit-learn": ("scikit-learn", "ml"),
    "PyTorch": ("torch", "ml"),
    "TensorFlow": ("tensorflow", "ml"),
}


def get_packages_in_category(category: str) -> tuple[str, ...]:
    """
    Return the display names registered under a category.

    Declaration order is preserved so that summary output is stable between
    captures on the same tool version.
    """
    return tuple(
        display_name
        for display_name, (_, package_category) in DEFAULT_PACKAGES.items()
        if package_category == category
    )

def get_package_version(package_name: str) -> str | None:
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
    packages: dict[str, tuple[str, str]] | None = None,
) -> dict[str, str | None]:
    """
    Return versions of selected Python packages.

    Packages that are unavailable in the current execution environment
    are represented by None. The emitted record is a flat display-name to
    version mapping; category is a capture-time concern and is deliberately
    not written into the record, so this change does not alter the schema
    of previously captured evidence.
    """
    packages = packages or DEFAULT_PACKAGES

    return {
        display_name: get_package_version(distribution_name)
        for display_name, (distribution_name, _) in packages.items()
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
