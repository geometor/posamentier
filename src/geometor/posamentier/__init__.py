"""Public package interface for ``geometor.posamentier``."""

from __future__ import annotations

from .app import main, run
from .catalog import CatalogEntrySpec, assert_no_floats, load_catalog_manifest
from .constructions import (
    CONSTRUCTION_BUILDERS,
    ConstructionSpec,
    build_construction,
    verify_golden_ratio,
)
from .svg import SvgHighlight, export_svg, render_model_svg

__version__ = "0.1.0"

__all__ = [
    "CONSTRUCTION_BUILDERS",
    "CatalogEntrySpec",
    "ConstructionSpec",
    "SvgHighlight",
    "__version__",
    "assert_no_floats",
    "build_construction",
    "export_svg",
    "load_catalog_manifest",
    "main",
    "render_model_svg",
    "run",
    "verify_golden_ratio",
]
