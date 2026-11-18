"""Tests for ``geometor.posamentier`` catalog, constructions, SVGs, and formulas."""

from __future__ import annotations

import pytest
import sympy as sp

from geometor.posamentier import (
    CONSTRUCTION_BUILDERS,
    CatalogEntrySpec,
    __version__,
    assert_no_floats,
    build_construction,
    load_catalog_manifest,
    run,
    verify_golden_ratio,
)
from geometor.posamentier.formulas import (
    verify_binet_fibonacci,
    verify_binet_lucas,
    verify_brahmagupta_area,
    verify_cassini_identity,
    verify_euler_oi_distance,
    verify_golden_cuboid,
    verify_heron_and_inradius,
    verify_kepler_triangle,
    verify_morley_trisector_side,
    verify_pentagonal_trig,
    verify_phi_power_linearization,
    verify_ptolemy_cyclic_quad,
    verify_stewart_theorem,
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
    assert len(entries) >= 22
    for item in entries:
        assert isinstance(item, CatalogEntrySpec)

    assert_no_floats(42)
    with pytest.raises(TypeError):
        assert_no_floats(1.618)
    with pytest.raises(TypeError):
        assert_no_floats(sp.Float("1.618"))


@pytest.mark.parametrize("entry_id", sorted(CONSTRUCTION_BUILDERS.keys()))
def test_exact_constructions_and_euclid_svg(entry_id: str) -> None:
    """Verify zero floats, exact phi ratio, and .euclid-graphic SVG output."""
    spec = build_construction(entry_id)
    ratio = verify_golden_ratio(spec)
    assert sp.simplify(ratio - sp.GoldenRatio) == 0
    svg = spec.to_svg()
    assert 'class="euclid-graphic"' in svg
    assert 'id="geom-tick-1"' in svg
    assert 'id="highlights"' in svg


def test_appendix_formulas() -> None:
    """Verify exact symbolic identities in the Appendix of Formulas."""
    for n in range(1, 9):
        verify_phi_power_linearization(n)
        verify_binet_fibonacci(n)
        verify_binet_lucas(n)
        verify_cassini_identity(n)

    trig = verify_pentagonal_trig()
    assert sp.simplify(trig["cos_36"] - sp.GoldenRatio / 2) == 0
    verify_kepler_triangle()
    diag, area = verify_golden_cuboid()
    assert sp.simplify(diag - 2 * sp.GoldenRatio) == 0
    assert_no_floats(area)

    # 13-14-15 Heron witness
    k, r, big_r = verify_heron_and_inradius(sp.Integer(13), sp.Integer(14), sp.Integer(15))
    assert k == 84
    assert r == 4
    assert big_r == sp.Rational(65, 8)
    assert verify_euler_oi_distance(sp.Integer(13), sp.Integer(14), sp.Integer(15)) == sp.Rational(
        65, 64
    )

    # Stewart on 3-4-5 right triangle median to hypotenuse (a=5, m=n=5/2, d=5/2)
    assert (
        verify_stewart_theorem(
            sp.Integer(5),
            sp.Integer(3),
            sp.Integer(4),
            sp.Rational(5, 2),
            sp.Rational(5, 2),
            sp.Rational(5, 2),
        )
        == 0
    )
    assert verify_ptolemy_cyclic_quad(sp.Integer(1)) == 0
    assert verify_brahmagupta_area(
        sp.Integer(3), sp.Integer(4), sp.Integer(3), sp.Integer(4)
    ) == 12
    assert_no_floats(verify_morley_trisector_side())
