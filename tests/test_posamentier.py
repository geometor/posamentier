"""Baseline tests for ``geometor.posamentier``."""

from __future__ import annotations

import pytest

from geometor.posamentier import (
    CatalogEntrySpec,
    __version__,
    assert_no_floats,
    load_catalog_manifest,
    run,
)


def test_version_and_cli() -> None:
    """Verify initial semantic version and clean zero-argument CLI execution."""
    assert __version__ == "0.1.0"
    assert run([]) == 0


def test_cli_help_exits_cleanly() -> None:
    """Verify ``--help`` exits cleanly with code ``0``."""
    with pytest.raises(SystemExit) as exc_info:
        run(["--help"])
    assert exc_info.value.code == 0


def test_catalog_manifest_and_float_guard() -> None:
    """Verify catalog manifest loading and floating-point prohibition guard."""
    entries = load_catalog_manifest()
    assert isinstance(entries, list)
    for item in entries:
        assert isinstance(item, CatalogEntrySpec)

    assert_no_floats(42)
    with pytest.raises(TypeError):
        assert_no_floats(1.618)
