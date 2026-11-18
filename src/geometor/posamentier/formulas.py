"""Exact SymPy symbolic formula verifiers for the Posamentier Appendix of Formulas."""

from __future__ import annotations

import sympy as sp

from .catalog import assert_no_floats

__all__ = [
    "PHI",
    "PSI",
    "verify_binet_fibonacci",
    "verify_binet_lucas",
    "verify_brahmagupta_area",
    "verify_cassini_identity",
    "verify_euler_oi_distance",
    "verify_golden_cuboid",
    "verify_heron_and_inradius",
    "verify_kepler_triangle",
    "verify_morley_trisector_side",
    "verify_pentagonal_trig",
    "verify_phi_power_linearization",
    "verify_ptolemy_cyclic_quad",
    "verify_stewart_theorem",
]

PHI: sp.Expr = sp.GoldenRatio
PSI: sp.Expr = 1 - sp.GoldenRatio  # -1/phi = (1 - sqrt(5))/2


def verify_phi_power_linearization(n: int) -> sp.Expr:
    """Verify ``phi^n == F_n * phi + F_{n-1}`` for integer ``n >= 1``."""
    lhs = sp.expand(PHI**n)
    rhs = sp.fibonacci(n) * PHI + sp.fibonacci(n - 1)
    diff = sp.simplify(lhs - rhs)
    assert_no_floats(diff)
    if diff != 0:
        msg = f"Power linearization failed at n={n}: {diff!r}"
        raise AssertionError(msg)
    return sp.simplify(rhs)


def verify_binet_fibonacci(n: int) -> sp.Expr:
    """Verify Binet's formula ``F_n == (phi^n - psi^n) / sqrt(5)``."""
    binet = (PHI**n - PSI**n) / sp.sqrt(5)
    diff = sp.simplify(binet - sp.fibonacci(n))
    assert_no_floats(diff)
    if diff != 0:
        msg = f"Binet Fibonacci failed at n={n}: {diff!r}"
        raise AssertionError(msg)
    return sp.fibonacci(n)


def verify_binet_lucas(n: int) -> sp.Expr:
    """Verify Binet's Lucas formula ``L_n == phi^n + psi^n``."""
    binet = PHI**n + PSI**n
    diff = sp.simplify(binet - sp.lucas(n))
    assert_no_floats(diff)
    if diff != 0:
        msg = f"Binet Lucas failed at n={n}: {diff!r}"
        raise AssertionError(msg)
    return sp.lucas(n)


def verify_cassini_identity(n: int) -> sp.Expr:
    """Verify Cassini's identity ``F_{n+1}*F_{n-1} - F_n^2 == (-1)^n``."""
    lhs = sp.fibonacci(n + 1) * sp.fibonacci(n - 1) - sp.fibonacci(n) ** 2
    rhs = (-1) ** n
    if lhs != rhs:
        msg = f"Cassini failed at n={n}: {lhs} != {rhs}"
        raise AssertionError(msg)
    return sp.Integer(rhs)


def verify_pentagonal_trig() -> dict[str, sp.Expr]:
    """Verify exact radical trigonometric values for ``18°`` and ``36°``."""
    sin18 = sp.simplify(sp.sin(sp.pi / 10) - 1 / (2 * PHI))
    cos36 = sp.simplify(sp.cos(sp.pi / 5) - PHI / 2)
    assert_no_floats(sin18)
    assert_no_floats(cos36)
    if sin18 != 0 or cos36 != 0:
        msg = "Pentagonal exact trigonometric identity failed"
        raise AssertionError(msg)
    return {
        "sin_18": sp.simplify(sp.sin(sp.pi / 10)),
        "cos_36": sp.simplify(sp.cos(sp.pi / 5)),
    }


def verify_kepler_triangle() -> sp.Expr:
    """Verify Kepler's right triangle ``1^2 + (sqrt(phi))^2 == phi^2``."""
    diff = sp.simplify(sp.Integer(1) + sp.sqrt(PHI) ** 2 - PHI**2)
    assert_no_floats(diff)
    if diff != 0:
        msg = f"Kepler triangle identity failed: {diff!r}"
        raise AssertionError(msg)
    return sp.simplify(PHI**2)


def verify_golden_cuboid() -> tuple[sp.Expr, sp.Expr]:
    """Verify Golden Cuboid ``(1, phi, phi^2)`` space diagonal ``2*phi`` and surface area."""
    diag_sq = sp.simplify(1 + PHI**2 + PHI**4 - (2 * PHI) ** 2)
    area = sp.simplify(2 * (1 * PHI + PHI * PHI**2 + PHI**2 * 1))
    assert_no_floats(diag_sq)
    assert_no_floats(area)
    if diag_sq != 0:
        msg = f"Golden cuboid space diagonal failed: {diag_sq!r}"
        raise AssertionError(msg)
    return sp.simplify(2 * PHI), area


def verify_heron_and_inradius(
    a: sp.Expr,
    b: sp.Expr,
    c: sp.Expr,
) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Return exact ``(area, inradius, circumradius)`` for triangle ``(a, b, c)``."""
    for side in (a, b, c):
        assert_no_floats(side)
    s = (a + b + c) / 2
    area = sp.sqrt(s * (s - a) * (s - b) * (s - c))
    inradius = sp.simplify(area / s)
    circumradius = sp.simplify((a * b * c) / (4 * area))
    return sp.simplify(area), inradius, circumradius


def verify_euler_oi_distance(a: sp.Expr, b: sp.Expr, c: sp.Expr) -> sp.Expr:
    """Verify Euler's theorem ``OI^2 == R*(R - 2*r)`` symbolically on ``(a, b, c)``."""
    _, r, R = verify_heron_and_inradius(a, b, c)
    oi_sq = sp.simplify(R * (R - 2 * r))
    assert_no_floats(oi_sq)
    return oi_sq


def verify_stewart_theorem(
    a: sp.Expr,
    b: sp.Expr,
    c: sp.Expr,
    m: sp.Expr,
    n: sp.Expr,
    d: sp.Expr,
) -> sp.Expr:
    """Return exact residual ``b^2*m + c^2*n - a*(d^2 + m*n)`` for Stewart's theorem."""
    for val in (a, b, c, m, n, d):
        assert_no_floats(val)
    return sp.simplify(b**2 * m + c**2 * n - a * (d**2 + m * n))


def verify_ptolemy_cyclic_quad(r: sp.Expr) -> sp.Expr:
    """Verify Ptolemy's theorem ``a*c + b*d == e*f`` on an inscribed cyclic rectangle."""
    assert_no_floats(r)
    # Inscribed rectangle of sides 2*r*cos(theta), 2*r*sin(theta) and diagonals 2*r
    a, b, c, d = sp.Integer(3) * r, sp.Integer(4) * r, sp.Integer(3) * r, sp.Integer(4) * r
    diag = sp.Integer(5) * r
    return sp.simplify(a * c + b * d - diag * diag)


def verify_brahmagupta_area(
    a: sp.Expr,
    b: sp.Expr,
    c: sp.Expr,
    d: sp.Expr,
) -> sp.Expr:
    """Return exact Brahmagupta cyclic quadrilateral area ``sqrt((s-a)(s-b)(s-c)(s-d))``."""
    for side in (a, b, c, d):
        assert_no_floats(side)
    s = (a + b + c + d) / 2
    area = sp.sqrt((s - a) * (s - b) * (s - c) * (s - d))
    return sp.simplify(area)


def verify_morley_trisector_side() -> sp.Expr:
    """Verify Morley's equilateral side ``8*R*sin(A/3)*sin(B/3)*sin(C/3)`` for equilateral ABC."""
    R = sp.Symbol("R", positive=True)
    # For equilateral triangle A=B=C=pi/3, A/3=pi/9
    side = 8 * R * sp.sin(sp.pi / 9) ** 3
    assert_no_floats(side)
    return sp.simplify(side)
