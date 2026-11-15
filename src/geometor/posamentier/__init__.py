"""Public package interface for ``geometor.posamentier``."""

from __future__ import annotations

from .app import main, run
from .catalog import CatalogEntrySpec, assert_no_floats, load_catalog_manifest

__version__ = "0.1.0"

__all__ = [
    "CatalogEntrySpec",
    "__version__",
    "assert_no_floats",
    "load_catalog_manifest",
    "main",
    "run",
]
