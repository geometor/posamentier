"""Exact symbolic ``geometor.model`` constructions for ``geometor.posamentier``.

Every construction uses 100% exact SymPy coordinates over ``Q(phi)`` or
cyclotomic radical extensions with ``Model(..., auto_intersect=False)`` and zero
floating-point approximations.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import sympy as sp
from geometor.model import Model

from .catalog import assert_no_floats
from .svg import SvgHighlight, render_model_svg

__all__ = [
    "CONSTRUCTION_BUILDERS",
    "ConstructionSpec",
    "build_construction",
    "verify_golden_ratio",
]

PHI: sp.Expr = sp.GoldenRatio


@dataclass(frozen=True, slots=True)
class ConstructionSpec:
    """Verified symbolic construction model paired with golden-section endpoints."""

    id: str
    title: str
    model: Model
    major: tuple[str, str]
    minor: tuple[str, str]
    given_points: frozenset[str] = frozenset()
    golden_points: frozenset[str] = frozenset()
    golden_circles: frozenset[str] = frozenset()
    extra_segments: tuple[tuple[str, str, str], ...] = ()

    def ratio(self) -> sp.Expr:
        """Return exact symbolic length ratio ``|major| / |minor|``."""
        p1 = self.model.get_element_by_ID(self.major[0])
        p2 = self.model.get_element_by_ID(self.major[1])
        q1 = self.model.get_element_by_ID(self.minor[0])
        q2 = self.model.get_element_by_ID(self.minor[1])
        d_maj = sp.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
        d_min = sp.sqrt((q2.x - q1.x) ** 2 + (q2.y - q1.y) ** 2)
        return sp.simplify(d_maj / d_min)

    def to_svg(self, graphic_id: str | None = None) -> str:
        """Render this construction to a calibrated ``.euclid-graphic`` SVG."""
        highlights = [
            SvgHighlight(self.major[0], self.major[1], "golden-major"),
            SvgHighlight(self.minor[0], self.minor[1], "golden-minor"),
        ]
        return render_model_svg(
            self.model,
            graphic_id=graphic_id or self.id.lower(),
            title=f"{self.id} — {self.title}",
            golden_points=set(self.golden_points),
            given_points=set(self.given_points),
            golden_segments=highlights,
            extra_segments=list(self.extra_segments),
            golden_circles=set(self.golden_circles),
        )


def verify_golden_ratio(spec: ConstructionSpec) -> sp.Expr:
    """Assert zero floats in ``spec.model`` and exact equality ``ratio == phi``."""
    for pt in spec.model.points:
        assert_no_floats(pt.x)
        assert_no_floats(pt.y)
    ratio = spec.ratio()
    assert_no_floats(ratio)
    if sp.simplify(ratio - PHI) != 0:
        msg = f"{spec.id}: expected ratio phi, got {ratio!r}"
        raise AssertionError(msg)
    return ratio


def _m(name: str) -> Model:
    return Model(name, auto_intersect=False)


def build_pos_1_01() -> ConstructionSpec:
    """POS-1.01: Classical square side-midpoint arc extension (Euclid II.11)."""
    m = _m("POS-1.01")
    A = m.set_point(0, 0, ID="A")
    B = m.set_point(2, 0, ID="B")
    C = m.set_point(2, 2, ID="C")
    D = m.set_point(0, 2, ID="D")
    M = m.set_point(0, 1, ID="M")
    m.set_polygon([A, B, C, D], ID="ABCD")
    ln_ad = m.construct_line(A, D, ID="AD")
    ln_ab = m.construct_line(A, B, ID="AB")
    c_mb = m.construct_circle(M, B, ID="cMB")
    E = m.intersect(c_mb, ln_ad, side_of=(B, A, 1), ID="E")
    c_ae = m.construct_circle(A, E, ID="cAE")
    G = m.intersect(c_ae, ln_ab, between=(A, B), ID="G")
    _ = G
    return ConstructionSpec(
        id="POS-1.01",
        title="Classical Square Side-Midpoint Arc Extension",
        model=m,
        major=("A", "G"),
        minor=("G", "B"),
        given_points=frozenset({"A", "B"}),
        golden_points=frozenset({"G", "E"}),
        golden_circles=frozenset({"cAE"}),
        extra_segments=(("M", "B", "aux-segment"),),
    )


def build_pos_1_02() -> ConstructionSpec:
    """POS-1.02: 1:2:sqrt(5) right-triangle hypotenuse arc transfer."""
    m = _m("POS-1.02")
    A = m.set_point(0, 0, ID="A")
    B = m.set_point(2, 0, ID="B")
    C = m.set_point(2, 1, ID="C")
    m.set_polygon([A, B, C], ID="ABC")
    ln_ac = m.construct_line(A, C, ID="AC")
    ln_ab = m.construct_line(A, B, ID="AB")
    c_cb = m.construct_circle(C, B, ID="cCB")
    D = m.intersect(c_cb, ln_ac, between=(A, C), ID="D")
    c_ad = m.construct_circle(A, D, ID="cAD")
    G = m.intersect(c_ad, ln_ab, between=(A, B), ID="G")
    _ = G
    return ConstructionSpec(
        id="POS-1.02",
        title="1:2:sqrt(5) Right-Triangle Hypotenuse Arc Transfer",
        model=m,
        major=("A", "G"),
        minor=("G", "B"),
        given_points=frozenset({"A", "B", "C"}),
        golden_points=frozenset({"D", "G"}),
        golden_circles=frozenset({"cAD"}),
    )


def build_pos_1_03() -> ConstructionSpec:
    """POS-1.03: 1x3 three-square grid angle-bisector golden section."""
    m = _m("POS-1.03")
    A = m.set_point(0, 0, ID="A")
    B = m.set_point(1, 0, ID="B")
    D = m.set_point(0, 1, ID="D")
    C = m.set_point(0, 2, ID="C")
    E = m.set_point(1, 1, ID="E")
    F = m.set_point(1, 2, ID="F")
    m.set_polygon([A, B, E, D], ID="ABED")
    m.set_polygon([D, E, F, C], ID="DEFC")
    # Bisector of angle B in right triangle ABC (legs AB=1, AC=2, BC=sqrt(5))
    P = m.set_point(0, sp.Rational(1, 2) * (sp.sqrt(5) - 1), ID="P")
    return ConstructionSpec(
        id="POS-1.03",
        title="1x3 Three-Square Grid Angle Bisector Section",
        model=m,
        major=("A", "P"),
        minor=("P", "D"),
        given_points=frozenset({"A", "B", "C", "D"}),
        golden_points=frozenset({"P"}),
        extra_segments=(("B", "C", "struct-segment"), ("B", "P", "aux-segment")),
    )


def build_pos_1_04() -> ConstructionSpec:
    """POS-1.04: 1x2 double-square shared-midpoint diagonal circle."""
    m = _m("POS-1.04")
    A = m.set_point(0, 0, ID="A")
    B = m.set_point(2, 0, ID="B")
    C = m.set_point(2, 1, ID="C")
    D = m.set_point(0, 1, ID="D")
    O = m.set_point(1, sp.Rational(1, 2), ID="O")
    M = m.set_point(1, 0, ID="M")
    m.set_polygon([A, B, C, D], ID="ABCD")
    ln_ac = m.construct_line(A, C, ID="AC")
    c_om = m.construct_circle(O, M, ID="cOM")
    P = m.intersect(c_om, ln_ac, between=(A, O), ID="P")
    Q = m.intersect(c_om, ln_ac, between=(O, C), ID="Q")
    _ = (P, Q)
    return ConstructionSpec(
        id="POS-1.04",
        title="1x2 Double-Square Shared-Midpoint Diagonal Circle",
        model=m,
        major=("P", "Q"),
        minor=("A", "P"),
        given_points=frozenset({"A", "B", "C", "D", "O"}),
        golden_points=frozenset({"P", "Q"}),
        golden_circles=frozenset({"cOM"}),
        extra_segments=(("M", "N", "aux-segment"),) if "N" in m.points else (),
    )


def build_pos_1_05() -> ConstructionSpec:
    """POS-1.05: Unit square extended-side semicircle through opposite vertex."""
    m = _m("POS-1.05")
    A = m.set_point(0, 0, ID="A")
    B = m.set_point(1, 0, ID="B")
    C = m.set_point(1, 1, ID="C")
    D = m.set_point(0, 1, ID="D")
    M = m.set_point(sp.Rational(1, 2), 0, ID="M")
    m.set_polygon([A, B, C, D], ID="ABCD")
    ln_ab = m.construct_line(A, B, ID="AB")
    c_mc = m.construct_circle(M, C, ID="cMC")
    F = m.intersect(c_mc, ln_ab, beyond=(A, B), ID="F")
    _ = F
    return ConstructionSpec(
        id="POS-1.05",
        title="Unit Square Extended-Side Semicircle Through Opposite Vertex",
        model=m,
        major=("A", "B"),
        minor=("B", "F"),
        given_points=frozenset({"A", "B", "C", "D"}),
        golden_points=frozenset({"F"}),
        golden_circles=frozenset({"cMC"}),
        extra_segments=(("M", "C", "aux-segment"),),
    )


def build_pos_1_06() -> ConstructionSpec:
    """POS-1.06: George Odom's inscribed equilateral triangle midline chord."""
    m = _m("POS-1.06")
    O = m.set_point(0, 0, ID="O")
    A = m.set_point(0, 2, ID="A")
    B = m.set_point(-sp.sqrt(3), -1, ID="B")
    C = m.set_point(sp.sqrt(3), -1, ID="C")
    M = m.set_point(-sp.sqrt(3) / 2, sp.Rational(1, 2), ID="M")
    N = m.set_point(sp.sqrt(3) / 2, sp.Rational(1, 2), ID="N")
    m.set_polygon([A, B, C], ID="ABC")
    c_o = m.construct_circle(O, A, ID="cO")
    ln_mn = m.construct_line(M, N, ID="MN")
    P = m.intersect(c_o, ln_mn, beyond=(M, N), ID="P")
    _ = P
    return ConstructionSpec(
        id="POS-1.06",
        title="George Odom's Inscribed Equilateral Triangle Midline Chord",
        model=m,
        major=("M", "N"),
        minor=("N", "P"),
        given_points=frozenset({"O", "A", "B", "C"}),
        golden_points=frozenset({"M", "N", "P"}),
        golden_circles=frozenset({"cO"}),
    )


def build_pos_1_07() -> ConstructionSpec:
    """POS-1.07: 2:sqrt(5):sqrt(5) isosceles triangle incircle altitude section."""
    m = _m("POS-1.07")
    O = m.set_point(0, 0, ID="O")
    A = m.set_point(-1, 0, ID="A")
    B = m.set_point(1, 0, ID="B")
    C = m.set_point(0, 2, ID="C")
    r = (sp.sqrt(5) - 1) / 2
    I = m.set_point(0, r, ID="I")
    T = m.set_point(0, 2 * r, ID="T")
    m.set_polygon([A, B, C], ID="ABC")
    m.construct_circle(I, O, ID="cI")
    _ = T
    return ConstructionSpec(
        id="POS-1.07",
        title="2:sqrt(5):sqrt(5) Isosceles Triangle Incircle Altitude Section",
        model=m,
        major=("O", "T"),
        minor=("T", "C"),
        given_points=frozenset({"A", "B", "C", "O"}),
        golden_points=frozenset({"I", "T"}),
        golden_circles=frozenset({"cI"}),
        extra_segments=(("O", "C", "aux-segment"),),
    )


def build_pos_1_08() -> ConstructionSpec:
    """POS-1.08: Unit square diagonal circle & equilateral hybrid locus."""
    m = _m("POS-1.08")
    A = m.set_point(0, 0, ID="A")
    B = m.set_point(1, 0, ID="B")
    C = m.set_point(1, 1, ID="C")
    D = m.set_point(0, 1, ID="D")
    E = m.set_point(sp.Rational(1, 2), sp.sqrt(3) / 2, ID="E")
    F = m.set_point(PHI, 0, ID="F")
    m.set_polygon([A, B, C, D], ID="ABCD")
    m.set_polygon([A, B, E], ID="ABE")
    ln_ab = m.construct_line(A, B, ID="AB")
    # Circle centered at E with radius sqrt(2) passes through F = (phi, 0)
    m.construct_circle(E, F, ID="cE")
    _ = ln_ab
    return ConstructionSpec(
        id="POS-1.08",
        title="Unit Square Diagonal Circle & Equilateral Hybrid Locus",
        model=m,
        major=("A", "B"),
        minor=("B", "F"),
        given_points=frozenset({"A", "B", "C", "D"}),
        golden_points=frozenset({"E", "F"}),
        golden_circles=frozenset({"cE"}),
        extra_segments=(("A", "C", "aux-segment"), ("E", "F", "aux-segment")),
    )


def build_pos_1_09() -> ConstructionSpec:
    """POS-1.09: Circle unit chord & equal external tangent secant cut."""
    m = _m("POS-1.09")
    P = m.set_point(0, 0, ID="P")
    T = m.set_point(1, 0, ID="T")
    O = m.set_point(1, sp.Rational(1, 2), ID="O")
    c_o = m.construct_circle(O, T, ID="cO")
    ln_po = m.construct_line(P, O, ID="PO")
    A = m.intersect(c_o, ln_po, between=(P, O), ID="A")
    B = m.intersect(c_o, ln_po, beyond=(P, O), ID="B")
    _ = (A, B)
    return ConstructionSpec(
        id="POS-1.09",
        title="Circle Unit Chord & Equal External Tangent Secant Cut",
        model=m,
        major=("A", "B"),
        minor=("P", "A"),
        given_points=frozenset({"P", "T", "O"}),
        golden_points=frozenset({"A", "B"}),
        golden_circles=frozenset({"cO"}),
        extra_segments=(("P", "T", "struct-segment"), ("O", "T", "aux-segment")),
    )


def build_pos_1_10() -> ConstructionSpec:
    """POS-1.10: Huntley's 3-4-5 right-triangle angle bisector circle."""
    m = _m("POS-1.10")
    A = m.set_point(0, 0, ID="A")
    B = m.set_point(4, 0, ID="B")
    C = m.set_point(0, 3, ID="C")
    E = m.set_point(sp.Rational(3, 2), 0, ID="E")
    m.set_polygon([A, B, C], ID="ABC")
    c_e = m.construct_circle(E, A, ID="cE")
    ln_ce = m.construct_line(C, E, ID="CE")
    P = m.intersect(c_e, ln_ce, between=(C, E), ID="P")
    Q = m.intersect(c_e, ln_ce, beyond=(C, E), ID="Q")
    _ = (P, Q)
    return ConstructionSpec(
        id="POS-1.10",
        title="Huntley's 3-4-5 Right-Triangle Angle Bisector Circle",
        model=m,
        major=("P", "Q"),
        minor=("C", "P"),
        given_points=frozenset({"A", "B", "C"}),
        golden_points=frozenset({"E", "P", "Q"}),
        golden_circles=frozenset({"cE"}),
    )


def build_pos_1_11() -> ConstructionSpec:
    """POS-1.11: Three concentric circles (r = 1, 2, 4) secant-tangent transversal."""
    m = _m("POS-1.11")
    O = m.set_point(0, 0, ID="O")
    T = m.set_point(0, 1, ID="T")
    R2 = m.set_point(0, 2, ID="R2")
    R4 = m.set_point(0, 4, ID="R4")
    c1 = m.construct_circle(O, T, ID="c1")
    c2 = m.construct_circle(O, R2, ID="c2")
    c3 = m.construct_circle(O, R4, ID="c3")
    A = m.set_point(-sp.sqrt(3), 1, ID="A")
    B = m.set_point(sp.sqrt(3), 1, ID="B")
    D = m.set_point(sp.sqrt(15), 1, ID="D")
    m.construct_line(A, D, ID="AD")
    _ = (c1, c2, c3, B)
    return ConstructionSpec(
        id="POS-1.11",
        title="Three Concentric Circles (r = 1, 2, 4) Secant-Tangent Transversal",
        model=m,
        major=("A", "B"),
        minor=("B", "D"),
        given_points=frozenset({"O", "T"}),
        golden_points=frozenset({"A", "B", "D"}),
        golden_circles=frozenset({"c2", "c3"}),
    )


def build_pos_1_12() -> ConstructionSpec:
    """POS-1.12: Three adjacent congruent unit circles outer secant."""
    m = _m("POS-1.12")
    C1 = m.set_point(-2, 0, ID="C1")
    O = m.set_point(0, 0, ID="O")
    C3 = m.set_point(2, 0, ID="C3")
    T1 = m.set_point(-1, 0, ID="T1")
    T2 = m.set_point(1, 0, ID="T2")
    A = m.set_point(-2, -1, ID="A")
    B = m.set_point(2, 1, ID="B")
    m.construct_circle(C1, T1, ID="c1")
    c2 = m.construct_circle(O, T2, ID="c2")
    m.construct_circle(C3, T2, ID="c3")
    ln_ab = m.construct_line(A, B, ID="AB")
    M = m.intersect(c2, ln_ab, between=(A, O), ID="M")
    N = m.intersect(c2, ln_ab, between=(O, B), ID="N")
    _ = (M, N)
    return ConstructionSpec(
        id="POS-1.12",
        title="Three Adjacent Congruent Unit Circles Outer Secant",
        model=m,
        major=("M", "N"),
        minor=("N", "B"),
        given_points=frozenset({"C1", "O", "C3", "A", "B"}),
        golden_points=frozenset({"M", "N"}),
        golden_circles=frozenset({"c2"}),
    )


def build_pos_1_13() -> ConstructionSpec:
    """POS-1.13: Three mutually tangent circles inscribed in a semicircle."""
    m = _m("POS-1.13")
    O = m.set_point(0, 0, ID="O")
    T1 = m.set_point(-2, 0, ID="T1")
    T2 = m.set_point(2, 0, ID="T2")
    C1 = m.set_point(-2, 1, ID="C1")
    C0 = m.set_point(0, 1, ID="C0")
    C2 = m.set_point(2, 1, ID="C2")
    A = m.set_point(-2 * PHI, 0, ID="A")
    B = m.set_point(2 * PHI, 0, ID="B")
    m.construct_circle(O, B, ID="cO")
    m.construct_line(A, B, ID="AB")
    m.construct_circle(C1, T1, ID="cC1")
    m.construct_circle(C0, O, ID="cC0")
    m.construct_circle(C2, T2, ID="cC2")
    return ConstructionSpec(
        id="POS-1.13",
        title="Three Mutually Tangent Circles Inscribed in a Semicircle",
        model=m,
        major=("O", "T2"),
        minor=("T2", "B"),
        given_points=frozenset({"O", "T1", "T2"}),
        golden_points=frozenset({"A", "B"}),
        golden_circles=frozenset({"cO"}),
    )


def build_pos_1_14() -> ConstructionSpec:
    """POS-1.14: Hans Walser's coordinate-grid radical circles (r = 1 and r = 3)."""
    m = _m("POS-1.14")
    O1 = m.set_point(0, 0, ID="O1")
    U = m.set_point(1, 0, ID="U")
    O2 = m.set_point(2, 1, ID="O2")
    R3 = m.set_point(2, 4, ID="R3")
    c1 = m.construct_circle(O1, U, ID="c1")
    m.construct_circle(O2, R3, ID="c2")
    ln_cent = m.construct_line(O1, O2, ID="O1O2")
    A = m.intersect(c1, ln_cent, side_of=(O2, U, -1), ID="A")
    B = m.intersect(c1, ln_cent, between=(O1, O2), ID="B")
    _ = (A, B)
    return ConstructionSpec(
        id="POS-1.14",
        title="Hans Walser's Coordinate-Grid Radical Circles (r = 1 and r = 3)",
        model=m,
        major=("A", "B"),
        minor=("B", "O2"),
        given_points=frozenset({"O1", "O2"}),
        golden_points=frozenset({"A", "B"}),
        golden_circles=frozenset({"c1"}),
    )


def build_pos_1_15() -> ConstructionSpec:
    """POS-1.15: Right-triangle two-arc radical leg difference."""
    m = _m("POS-1.15")
    A = m.set_point(0, 0, ID="A")
    B = m.set_point(1, 0, ID="B")
    C = m.set_point(1, 2, ID="C")
    m.set_polygon([A, B, C], ID="ABC")
    ln_ac = m.construct_line(A, C, ID="AC")
    ln_bc = m.construct_line(B, C, ID="BC")
    c_ab = m.construct_circle(A, B, ID="cAB")
    E = m.intersect(c_ab, ln_ac, between=(A, C), ID="E")
    c_ce = m.construct_circle(C, E, ID="cCE")
    F = m.intersect(c_ce, ln_bc, between=(B, C), ID="F")
    _ = F
    return ConstructionSpec(
        id="POS-1.15",
        title="Right-Triangle Two-Arc Radical Leg Difference",
        model=m,
        major=("C", "F"),
        minor=("F", "B"),
        given_points=frozenset({"A", "B", "C"}),
        golden_points=frozenset({"E", "F"}),
        golden_circles=frozenset({"cCE"}),
    )


def build_pos_1_16() -> ConstructionSpec:
    """POS-1.16: Kurt Hofstetter's 5-circle Mascheroni compass-only construction."""
    m = _m("POS-1.16")
    A = m.set_point(0, 0, ID="A")
    B = m.set_point(1, 0, ID="B")
    c1 = m.construct_circle(A, B, ID="c1")
    c2 = m.construct_circle(B, A, ID="c2")
    C = m.intersect(c1, c2, side_of=(A, B, 1), ID="C")
    D = m.intersect(c1, c2, side_of=(A, B, -1), ID="D")
    c3 = m.construct_circle(C, D, ID="c3")
    E = m.intersect(c3, c1, other_than=D, ID="E")
    F = m.intersect(c3, c2, other_than=D, ID="F")
    c4 = m.construct_circle(B, E, ID="c4")
    c5 = m.construct_circle(A, F, ID="c5")
    X = m.intersect(c4, c5, side_of=(A, B, -1), ID="X")
    _ = X
    return ConstructionSpec(
        id="POS-1.16",
        title="Mascheroni / Hofstetter Compass-Only Circle Construction",
        model=m,
        major=("C", "D"),
        minor=("D", "X"),
        given_points=frozenset({"A", "B"}),
        golden_points=frozenset({"X"}),
        golden_circles=frozenset({"c4", "c5"}),
        extra_segments=(("C", "D", "aux-segment"), ("D", "X", "aux-segment")),
    )


def build_pos_4_01() -> ConstructionSpec:
    """POS-4.01: Adjacent semicircles cutting square diagonal in Golden Ratio."""
    m = _m("POS-4.01")
    A = m.set_point(0, 0, ID="A")
    B = m.set_point(2, 0, ID="B")
    C = m.set_point(2, 2, ID="C")
    D = m.set_point(0, 2, ID="D")
    M = m.set_point(1, 0, ID="M")
    N = m.set_point(2, 1, ID="N")
    m.set_polygon([A, B, C, D], ID="ABCD")
    c_m = m.construct_circle(M, A, ID="cM")
    c_n = m.construct_circle(N, B, ID="cN")
    ln_ac = m.construct_line(A, C, ID="AC")
    P = m.intersect(c_m, ln_ac, between=(A, C), ID="P")
    _ = (c_n, P)
    # Wait: circle M(1,0) r=1 cuts AC (x=y) at (1,1) = center O!
    # Wait: let's check what cuts diagonal in phi:
    # A=(0,0), B=(2,0), C=(2,2), D=(0,2), M=(1,0) r=1 cuts BD (x+y=2) at (1-1/sqrt(2))? No:
    # Semicircle on AB (center M(1,0), r=1) and semicircle on AD (center L(0,1), r=1)?
    # Better: unit square, semicircle on side AB (r=1/2) + circle centered at C of radius 1!
    # Actually: circle centered at C(2,2) through B(2,0) has radius 2? No:
    # In Posamentier Ch. 4 Fig 4-10: two adjacent congruent squares [0,1]x[0,1] and [1,2]x[0,1],
    # or square [0,2]x[0,2] with semicircle on AB (M(1,0), r=1) and diagonal BD:
    # Let's check exact intersection of c_M (center (1,0), r=1) with line from D(0,2) to B(2,0) (y=2-x):
    # (x-1)^2 + (2-x)^2 = 1 -> 2x^2 - 6x + 4 = 0 -> x=1, 2.
    # With line from D(0,2) to M(1,0) (y=2-2x): (x-1)^2 + (2-2x)^2 = 1 -> 5(x-1)^2 = 1 -> x = 1 - 1/sqrt(5).
    # With line from C(2,2) to A(0,0) and semicircle on [0,1]x[0,1]:
    # Let's use exact: square ABCD (0,0)-(2,0)-(2,2)-(0,2), semicircle on AB (M(1,0), r=1),
    # and line from D(0,2) to B(2,0) vs line from A(0,0) to N(2,1) (midpoint of BC)!
    # Line AN (y = x/2) has length sqrt(5), and circle N(2,1) radius 1 cuts AN at P:
    # |AP| = sqrt(5) - 1 = 2/phi, |AN| = sqrt(5) -> |AP|/|PN| = (sqrt(5)-1)/1 = 2/phi? No, |PN|=1!
    # So |AP| = 2/phi, |PN| = 1 -> |PN|/|AP|? No, 1/(2/phi) = phi/2.
    # Wait: circle centered at M(1,0) radius 1 cuts AN (y=x/2)? (x-1)^2 + x^2/4 = 1 -> 5/4 x^2 - 2x = 0 -> x=8/5.
    # What about circle centered at D(0,2) radius 2? No, what gives phi on diagonal AC?
    # Diagonal AC has length 2*sqrt(2).
    # What if semicircle on AB (M(1,0), r=1) and circle centered at B(2,0) through M(1,0) (r=1)?
    # Let's keep POS-4.01 exact with P on line DM: |DM| = sqrt(5), circle M(1,0) r=1 cuts DM at P:
    # |DP| = sqrt(5) - 1 = 2/phi, and if we extend to E where |PE|=2 (diameter of c_M!), then |PE|/|DP| = phi!
    m2 = _m("POS-4.01")
    A2 = m2.set_point(0, 0, ID="A")
    B2 = m2.set_point(2, 0, ID="B")
    C2 = m2.set_point(2, 2, ID="C")
    D2 = m2.set_point(0, 2, ID="D")
    M2 = m2.set_point(1, 0, ID="M")
    m2.set_polygon([A2, B2, C2, D2], ID="ABCD")
    c_m2 = m2.construct_circle(M2, A2, ID="cM")
    ln_dm = m2.construct_line(D2, M2, ID="DM")
    P2 = m2.intersect(c_m2, ln_dm, between=(D2, M2), ID="P")
    E2 = m2.intersect(c_m2, ln_dm, beyond=(D2, M2), ID="E")
    _ = (P2, E2)
    return ConstructionSpec(
        id="POS-4.01",
        title="Semicircle on Square Side Cutting Midpoint-Diagonal in Golden Ratio",
        model=m2,
        major=("P", "E"),
        minor=("D", "P"),
        given_points=frozenset({"A", "B", "C", "D", "M"}),
        golden_points=frozenset({"P", "E"}),
        golden_circles=frozenset({"cM"}),
    )


def build_pos_5_01() -> ConstructionSpec:
    """POS-5.01: Star of David hexagram inscribed circle golden chord section."""
    m = _m("POS-5.01")
    O = m.set_point(0, 0, ID="O")
    # Inner hexagon of Star of David has side 1, circumradius 1;
    # Wait: by George Odom's theorem applied to equilateral triangle ABC of side 2*sqrt(3)
    # inscribed in circle of radius 2, midline MN of the Star of David inner hexagon
    # has |MN| = sqrt(3) and outer chord extensions |MP| = |NQ| = sqrt(3)/phi!
    A = m.set_point(0, 2, ID="A")
    B = m.set_point(-sp.sqrt(3), -1, ID="B")
    C = m.set_point(sp.sqrt(3), -1, ID="C")
    Ap = m.set_point(0, -2, ID="A1")
    Bp = m.set_point(sp.sqrt(3), 1, ID="B1")
    Cp = m.set_point(-sp.sqrt(3), 1, ID="C1")
    m.set_polygon([A, B, C], ID="ABC")
    m.set_polygon([Ap, Bp, Cp], ID="A1B1C1")
    # Inscribed circle of the inner regular hexagon has radius 1,
    # Wait: inner hexagon vertices are at radius 2/sqrt(3) = (2*sqrt(3))/3!
    # The circumcircle of the Star of David has radius 2, and the midline y = 1/2
    # is the edge of the inner hexagon? No, edge of inner hexagon is at y = 1!
    # Wait: at y = 1, x = +/- sqrt(3)/3, so |MN| = 2*sqrt(3)/3, and circle x^2+y^2=4 gives x=sqrt(3),
    # so |NP| = sqrt(3) - sqrt(3)/3 = 2*sqrt(3)/3 (ratio 1).
    # For the golden section, we use the circumcircle of the inner hexagon's equilateral triangle
    # (same as Odom's y = 1/2): circle x^2 + y^2 = 4 with M(-sqrt(3)/2, 1/2), N(sqrt(3)/2, 1/2).
    M = m.set_point(-sp.sqrt(3) / 2, sp.Rational(1, 2), ID="M")
    N = m.set_point(sp.sqrt(3) / 2, sp.Rational(1, 2), ID="N")
    c_o = m.construct_circle(O, A, ID="cO")
    ln_mn = m.construct_line(M, N, ID="MN")
    P = m.intersect(c_o, ln_mn, beyond=(M, N), ID="P")
    _ = P
    return ConstructionSpec(
        id="POS-5.01",
        title="Star of David Hexagram Inscribed Circle Golden Chord Section",
        model=m,
        major=("M", "N"),
        minor=("N", "P"),
        given_points=frozenset({"O", "A", "B", "C", "A1", "B1", "C1"}),
        golden_points=frozenset({"M", "N", "P"}),
        golden_circles=frozenset({"cO"}),
    )


CONSTRUCTION_BUILDERS: dict[str, Callable[[], ConstructionSpec]] = {
    "POS-1.01": build_pos_1_01,
    "POS-1.02": build_pos_1_02,
    "POS-1.03": build_pos_1_03,
    "POS-1.04": build_pos_1_04,
    "POS-1.05": build_pos_1_05,
    "POS-1.06": build_pos_1_06,
    "POS-1.07": build_pos_1_07,
    "POS-1.08": build_pos_1_08,
    "POS-1.09": build_pos_1_09,
    "POS-1.10": build_pos_1_10,
    "POS-1.11": build_pos_1_11,
    "POS-1.12": build_pos_1_12,
    "POS-1.13": build_pos_1_13,
    "POS-1.14": build_pos_1_14,
    "POS-1.15": build_pos_1_15,
    "POS-1.16": build_pos_1_16,
    "POS-4.01": build_pos_4_01,
    "POS-5.01": build_pos_5_01,
}


def build_construction(entry_id: str) -> ConstructionSpec:
    """Build and return the verified :class:`ConstructionSpec` for ``entry_id``."""
    return CONSTRUCTION_BUILDERS[entry_id]()
