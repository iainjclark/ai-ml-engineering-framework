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
from packaging.version import Version

import platform

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
    # Numerics / dataframe / statistical computing
    "NumPy": ("numpy", "numerics"),
    "SciPy": ("scipy", "numerics"),
    "pandas": ("pandas", "numerics"),
    "pyarrow": ("pyarrow", "numerics"),
    "polars": ("polars", "numerics"),
    "statsmodels": ("statsmodels", "numerics"),
    "JAX": ("jax", "numerics"),
    "jaxlib": ("jaxlib", "numerics"),

    # AI / ML frameworks and libraries
    "scikit-learn": ("scikit-learn", "ml"),
    "PyTorch": ("torch", "ml"),
    "TensorFlow": ("tensorflow", "ml"),
    "Keras": ("keras", "ml"),
    "XGBoost": ("xgboost", "ml"),
    "LightGBM": ("lightgbm", "ml"),
    "CatBoost": ("catboost", "ml"),
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

def get_pytorch_gpu_diagnostics() -> dict[str, Any]:
    """
    Test whether the installed PyTorch runtime can execute on a supported GPU.

    A successful result requires:
        1. A GPU-capable PyTorch backend.
        2. At least one usable GPU device visible to PyTorch.
        3. A real tensor computation to complete successfully.

    Supported backends:
        - CUDA
        - Apple Metal Performance Shaders (MPS)

    Failure is recorded rather than raised so that diagnostics remain usable
    on CPU-only systems and systems with incomplete accelerator configuration.
    """
    result: dict[str, Any] = {
        "GPU Build": False,
        "GPU Detected": False,
        "Smoke Test Passed": False,
        "Backend": None,
        "Device": None,
    }

    # Do not import PyTorch unless it is actually installed.
    if get_package_version("torch") is None:
        return result

    try:
        import torch

        # CUDA path.
        cuda_version = torch.version.cuda

        if cuda_version is not None:
            result["GPU Build"] = True
            result["Backend"] = f"CUDA {cuda_version}"

            if not torch.cuda.is_available():
                return result

            if torch.cuda.device_count() < 1:
                return result

            result["GPU Detected"] = True
            result["Device"] = torch.cuda.get_device_name(0)

            x = torch.tensor(
                [1.0, 2.0],
                dtype=torch.float32,
                device="cuda",
            )

            y = (x * x).sum()

            # Force completion of CUDA work before declaring success.
            torch.cuda.synchronize()

            result["Smoke Test Passed"] = (
                y.device.type == "cuda"
                and y.item() == 5.0
            )

            return result

        # Apple Silicon / MPS path.
        if (
            hasattr(torch.backends, "mps")
            and torch.backends.mps.is_built()
        ):
            result["GPU Build"] = True
            result["Backend"] = "MPS"

            if not torch.backends.mps.is_available():
                return result

            result["GPU Detected"] = True
            result["Device"] = "mps:0"

            x = torch.tensor(
                [1.0, 2.0],
                dtype=torch.float32,
                device="mps",
            )

            y = (x * x).sum()

            result["Smoke Test Passed"] = (
                y.device.type == "mps"
                and y.item() == 5.0
            )

    except Exception as exc:
        # Diagnostics should describe a broken accelerator stack rather than
        # causing the entire system diagnostic capture to fail.
        result["Error"] = f"{type(exc).__name__}: {exc}"

    return result
    
def get_tensorflow_gpu_diagnostics() -> dict[str, Any]:
    """
    Test whether the installed TensorFlow runtime can execute on a GPU.
    """

    result: dict[str, Any] = {
        "GPU Build": False,
        "GPU Detected": False,
        "Smoke Test Passed": False,
        "Backend": None,
        "Device": None,
    }

    tf_version = get_package_version("tensorflow")

    if tf_version is None:
        return result

    # TensorFlow >= 2.11 does not support native-Windows CUDA.
    # Avoid importing TensorFlow unnecessarily, which also avoids its
    # verbose C++ startup messages in the diagnostic console output.
    if (
        platform.system() == "Windows"
        and Version(tf_version) >= Version("2.11")
    ):
        result["Reason"] = (
            "Native Windows CUDA unsupported by TensorFlow >= 2.11"
        )
        return result

    import os
    os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")

    try:
        import tensorflow as tf

        gpus = tf.config.list_physical_devices("GPU")

        if not gpus:
            return result

        result["GPU Build"] = True
        result["GPU Detected"] = True

        if tf.test.is_built_with_cuda():
            build_info = tf.sysconfig.get_build_info()
            cuda_version = build_info.get("cuda_version")

            result["Backend"] = (
                f"CUDA {cuda_version}"
                if cuda_version
                else "CUDA"
            )

        elif platform.system() == "Darwin":
            result["Backend"] = "Metal"

        else:
            result["Backend"] = "GPU"

        details = tf.config.experimental.get_device_details(gpus[0])
        result["Device"] = (
            details.get("device_name")
            or gpus[0].name
        )

        with tf.device("/GPU:0"):
            a = tf.constant(
                [[1.0, 2.0], [3.0, 4.0]],
                dtype=tf.float32,
            )
            b = tf.linalg.matmul(a, a)

        value = float(tf.reduce_sum(b).numpy())
        ran_on_gpu = "GPU" in b.device.upper()

        result["Smoke Test Passed"] = (
            ran_on_gpu
            and abs(value - 54.0) < 1e-6
        )

    except Exception as exc:
        result["Error"] = f"{type(exc).__name__}: {exc}"

    return result
    
def get_software_diagnostics() -> dict[str, Any]:
    """
    Capture a structured software-stack diagnostic snapshot.
    """
    return {
        "Packages": get_package_versions(),
        "Accelerators": {
            "PyTorch": get_pytorch_gpu_diagnostics(),
            "TensorFlow": get_tensorflow_gpu_diagnostics(),
        },        
        
    }

if __name__ == "__main__":
    from pprint import pprint

    pprint(get_software_diagnostics())
