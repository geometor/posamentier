"""Theme-adaptive ``.euclid-graphic`` SVG renderer for ``geometor.posamentier``.

Generates publication-grade interactive SVGs from exact symbolic
:class:`~geometor.model.Model` constructions, conforming to the PHOTON Publish
Book Codex contract (``svg.euclid-graphic``, ``#geom-tick-1..3``,
``prefers-color-scheme: dark``, 3-vertex ``<path>`` segments, and canonical
``data-ref`` / ``data-aliases`` attributes for ``geometor_interactive.js``).
"""

from __future__ import annotations

import html
import math
from dataclasses import dataclass, field
from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

__all__ = [
    "EMBEDDED_SVG_STYLE",
    "SvgHighlight",
    "export_svg",
    "render_model_svg",
]

EMBEDDED_SVG_STYLE: str = """
  .euclid-graphic {
    font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  }
  .euclid-graphic .svg-bg { fill: none; }
  .euclid-graphic .geom-circle.conic-curve { fill: none; stroke: #0284c7; stroke-width: 1.85; stroke-opacity: 0.82; }
  .euclid-graphic .geom-circle.aux-circle { fill: none; stroke: #0369a1; stroke-width: 1.35; stroke-dasharray: 5 3.5; stroke-opacity: 0.62; }
  .euclid-graphic .geom-circle.golden-circle { fill: none; stroke: #d4af37; stroke-width: 2.35; stroke-opacity: 0.92; }
  .euclid-graphic .geom-polygon.poly-shape { fill: #0284c7; fill-opacity: 0.07; stroke: #334155; stroke-width: 1.85; stroke-linejoin: round; }
  .euclid-graphic .geom-polygon.golden-poly { fill: #d4af37; fill-opacity: 0.11; stroke: #d4af37; stroke-width: 2.1; stroke-linejoin: round; }
  .euclid-graphic .geom-line { fill: none; stroke: #475569; stroke-width: 1.45; stroke-linecap: round; stroke-opacity: 0.72; }
  .euclid-graphic .geom-line.aux-line { fill: none; stroke: #64748b; stroke-width: 1.2; stroke-dasharray: 5 3.5; stroke-opacity: 0.58; }
  .euclid-graphic .geom-segment.struct-segment { fill: none; stroke: #334155; stroke-width: 1.95; stroke-linecap: round; stroke-opacity: 0.88; }
  .euclid-graphic .geom-segment.aux-segment { fill: none; stroke: #64748b; stroke-width: 1.35; stroke-dasharray: 4.5 3; stroke-linecap: round; stroke-opacity: 0.68; }
  .euclid-graphic .geom-segment.golden-major-glow { fill: none; stroke: #d4af37; stroke-opacity: 0.28; stroke-width: 9.5; stroke-linecap: round; pointer-events: none; }
  .euclid-graphic .geom-segment.golden-major { fill: none; stroke: #d4af37; color: #78350f; stroke-width: 4.3; stroke-linecap: round; }
  .euclid-graphic .geom-segment.golden-minor { fill: none; stroke: #c2410c; color: #7c2d12; stroke-width: 3.7; stroke-linecap: round; }
  .euclid-graphic .geom-overlay { fill: none; stroke: none; stroke-width: 10; stroke-linecap: round; opacity: 0; pointer-events: none; }
  .euclid-graphic .geom-point { fill: #0369a1; stroke: #fafaf9; stroke-width: 1.5; }
  .euclid-graphic .geom-point.given-point { fill: #0f172a; }
  .euclid-graphic .geom-point.golden-point { fill: #d4af37; stroke: #1c1917; stroke-width: 1.7; }
  .euclid-graphic .geom-point-halo { fill: none; stroke: #d4af37; stroke-opacity: 0.55; stroke-width: 1.8; pointer-events: none; }
  .euclid-graphic .geom-label {
    fill: #1c1917;
    font-size: 13.5px;
    font-weight: 600;
    paint-order: stroke fill;
    stroke: #fafaf9;
    stroke-opacity: 0.92;
    stroke-width: 3.6px;
    stroke-linejoin: round;
    user-select: none;
  }
  @media (prefers-color-scheme: dark) {
    .euclid-graphic .geom-circle.conic-curve { stroke: #38bdf8; }
    .euclid-graphic .geom-circle.aux-circle { stroke: #7dd3fc; }
    .euclid-graphic .geom-circle.golden-circle { stroke: #f5c542; }
    .euclid-graphic .geom-polygon.poly-shape { fill: #38bdf8; stroke: #cbd5e1; }
    .euclid-graphic .geom-polygon.golden-poly { fill: #f5c542; stroke: #f5c542; }
    .euclid-graphic .geom-line { stroke: #94a3b8; }
    .euclid-graphic .geom-line.aux-line { stroke: #64748b; }
    .euclid-graphic .geom-segment.struct-segment { stroke: #cbd5e1; }
    .euclid-graphic .geom-segment.aux-segment { stroke: #64748b; }
    .euclid-graphic .geom-segment.golden-major-glow { stroke: #f5c542; stroke-opacity: 0.32; }
    .euclid-graphic .geom-segment.golden-major { stroke: #f5c542; color: #fef3c7; }
    .euclid-graphic .geom-segment.golden-minor { stroke: #fb923c; color: #ffedd5; }
    .euclid-graphic .geom-point { fill: #38bdf8; stroke: #141417; }
    .euclid-graphic .geom-point.given-point { fill: #e2e8f0; }
    .euclid-graphic .geom-point.golden-point { fill: #f5c542; stroke: #141417; }
    .euclid-graphic .geom-point-halo { stroke: #f5c542; }
    .euclid-graphic .geom-label { fill: #f4f4f5; stroke: #141417; }
  }
""".strip()

_TICK_DEFS: str = """  <defs>
    <marker id="geom-tick-1" markerUnits="userSpaceOnUse" viewBox="-5 -8 10 16" markerWidth="10" markerHeight="16" orient="auto">
      <line x1="0" y1="-6.2" x2="0" y2="6.2" stroke="currentColor" stroke-width="1.85" stroke-linecap="round" />
    </marker>
    <marker id="geom-tick-2" markerUnits="userSpaceOnUse" viewBox="-7 -8 14 16" markerWidth="14" markerHeight="16" orient="auto">
      <line x1="-2.4" y1="-6.2" x2="-2.4" y2="6.2" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" />
      <line x1="2.4" y1="-6.2" x2="2.4" y2="6.2" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" />
    </marker>
    <marker id="geom-tick-3" markerUnits="userSpaceOnUse" viewBox="-9 -8 18 16" markerWidth="18" markerHeight="16" orient="auto">
      <line x1="-4.4" y1="-6.2" x2="-4.4" y2="6.2" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" />
      <line x1="0" y1="-6.2" x2="0" y2="6.2" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" />
      <line x1="4.4" y1="-6.2" x2="4.4" y2="6.2" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" />
    </marker>
  </defs>"""


@dataclass(frozen=True, slots=True)
class SvgHighlight:
    """Specification for a golden-section segment pair highlighted in an SVG."""

    p1: str
    p2: str
    role: str = "golden-major"  # "golden-major" | "golden-minor" | "struct-segment" | "aux-segment"


@dataclass(slots=True)
class _Viewport:
    """Affine world-to-SVG coordinate mapper."""

    xmin: float
    xmax: float
    ymin: float
    ymax: float
    width: int = 680
    height: int = 480
    pad: float = 42.0
    scale: float = field(init=False)
    cx: float = field(init=False)
    cy: float = field(init=False)

    def __post_init__(self) -> None:
        span_x = max(self.xmax - self.xmin, 1e-6)
        span_y = max(self.ymax - self.ymin, 1e-6)
        usable_w = self.width - 2.0 * self.pad
        usable_h = self.height - 2.0 * self.pad
        self.scale = min(usable_w / span_x, usable_h / span_y)
        self.cx = 0.5 * (self.xmin + self.xmax)
        self.cy = 0.5 * (self.ymin + self.ymax)

    def to_svg(self, x: float, y: float) -> tuple[float, float]:
        sx = 0.5 * self.width + (x - self.cx) * self.scale
        sy = 0.5 * self.height - (y - self.cy) * self.scale
        return sx, sy


def _fmt(val: float) -> str:
    if abs(val - round(val)) < 1e-4:
        return str(round(val))
    return f"{val:.2f}".rstrip("0").rstrip(".")


def _esc(val: str) -> str:
    return html.escape(val, quote=True)


def _three_vertex_path(x1: float, y1: float, x2: float, y2: float) -> str:
    mx = 0.5 * (x1 + x2)
    my = 0.5 * (y1 + y2)
    return f"M {_fmt(x1)} {_fmt(y1)} L {_fmt(mx)} {_fmt(my)} L {_fmt(x2)} {_fmt(y2)}"


def _clip_line(
    line: spg.Line,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
) -> tuple[tuple[float, float], tuple[float, float]] | None:
    a_f = float(line.coefficients[0].evalf())
    b_f = float(line.coefficients[1].evalf())
    c_f = float(line.coefficients[2].evalf())
    eps = 1e-9
    hits: list[tuple[float, float]] = []
    if abs(b_f) > eps:
        for xv in (xmin, xmax):
            yv = -(a_f * xv + c_f) / b_f
            if ymin - eps <= yv <= ymax + eps:
                hits.append((xv, yv))
    if abs(a_f) > eps:
        for yv in (ymin, ymax):
            xv = -(b_f * yv + c_f) / a_f
            if xmin - eps <= xv <= xmax + eps:
                hits.append((xv, yv))
    unique: list[tuple[float, float]] = []
    for pt in hits:
        if not any(math.hypot(pt[0] - u[0], pt[1] - u[1]) < 1e-5 for u in unique):
            unique.append(pt)
    if len(unique) < 2:
        return None
    return unique[0], unique[1]


def _point_xy(pt: spg.Point2D) -> tuple[float, float]:
    return float(pt.x.evalf()), float(pt.y.evalf())


def render_model_svg(
    model: Model,
    graphic_id: str,
    title: str,
    *,
    golden_points: set[str] | None = None,
    given_points: set[str] | None = None,
    golden_segments: list[SvgHighlight] | None = None,
    extra_segments: list[tuple[str, str, str]] | None = None,
    golden_circles: set[str] | None = None,
    width: int = 680,
    height: int = 480,
) -> str:
    """Render a :class:`~geometor.model.Model` as a calibrated ``.euclid-graphic`` SVG.

    Args:
        model: Exact symbolic geometry model.
        graphic_id: Identifier placed in ``data-graphic-id``.
        title: Human-readable title and ``aria-label``.
        golden_points: Point IDs rendered with a golden halo.
        given_points: Point IDs styled as base given points.
        golden_segments: Highlighted golden-major / golden-minor / structural segments.
        extra_segments: Additional ``(p1, p2, css_class)`` segments to draw.
        golden_circles: Circle IDs styled as golden circles.
        width: SVG viewport width in pixels.
        height: SVG viewport height in pixels.

    Returns:
        Complete ``<svg class="euclid-graphic" ...>...</svg>`` markup.
    """
    golden_pts = golden_points or set()
    given_pts = given_points or set()
    golden_circs = golden_circles or set()

    coords: dict[str, tuple[float, float]] = {
        model[pt].ID: _point_xy(pt) for pt in model.points
    }
    xs = [c[0] for c in coords.values()]
    ys = [c[1] for c in coords.values()]

    for circ in model.circles:
        cx = float(circ.center.x.evalf())
        cy = float(circ.center.y.evalf())
        r = abs(float(circ.radius.evalf()))
        xs.extend([cx - r, cx + r])
        ys.extend([cy - r, cy + r])

    if not xs or not ys:
        xs, ys = [-1.0, 1.0], [-1.0, 1.0]

    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    pad_world = 0.08 * max(xmax - xmin, ymax - ymin, 1.0)
    vp = _Viewport(
        xmin - pad_world,
        xmax + pad_world,
        ymin - pad_world,
        ymax + pad_world,
        width=width,
        height=height,
    )

    graphics_lines: list[str] = []
    highlights_lines: list[str] = []

    # 1. Circles
    for circ in model.circles:
        cid = model[circ].ID
        cx_w, cy_w = _point_xy(circ.center)
        r_w = abs(float(circ.radius.evalf()))
        scx, scy = vp.to_svg(cx_w, cy_w)
        sr = r_w * vp.scale
        cls = "geom-circle golden-circle" if cid in golden_circs else "geom-circle aux-circle"
        graphics_lines.append(
            f'      <circle class="{cls}" cx="{_fmt(scx)}" cy="{_fmt(scy)}" '
            f'r="{_fmt(sr)}" data-ref="{_esc(cid)}" fill="none">'
            f"<title>{_esc(cid)}</title></circle>"
        )

    # 2. Polygons
    for poly in model.polygons:
        poly_id = model[poly].ID
        pts_svg = [vp.to_svg(*_point_xy(v)) for v in poly.vertices]
        pts_attr = " ".join(f"{_fmt(px)},{_fmt(py)}" for px, py in pts_svg)
        v_names = " ".join(
            model[v].ID if v in model else ""
            for v in poly.vertices
        ).strip()
        ref = f"< {v_names} >" if v_names else poly_id
        graphics_lines.append(
            f'      <polygon class="geom-polygon poly-shape" points="{pts_attr}" '
            f'data-ref="{_esc(ref)}" data-aliases="{_esc(poly_id)}" />'
        )

    # 3. Lines (clipped to world viewport)
    for line_obj in model.lines:
        lid = model[line_obj].ID
        clipped = _clip_line(line_obj, vp.xmin, vp.xmax, vp.ymin, vp.ymax)
        if clipped is None:
            continue
        p1_s = vp.to_svg(*clipped[0])
        p2_s = vp.to_svg(*clipped[1])
        d_attr = _three_vertex_path(p1_s[0], p1_s[1], p2_s[0], p2_s[1])
        graphics_lines.append(
            f'      <path class="geom-line aux-line" d="{d_attr}" '
            f'data-ref="{_esc(lid)}" fill="none"><title>{_esc(lid)}</title></path>'
        )

    # 4. Model segments
    for seg in model.segments:
        sid = model[seg].ID
        p1_s = vp.to_svg(*_point_xy(seg.p1))
        p2_s = vp.to_svg(*_point_xy(seg.p2))
        d_attr = _three_vertex_path(p1_s[0], p1_s[1], p2_s[0], p2_s[1])
        graphics_lines.append(
            f'      <path class="geom-segment struct-segment" d="{d_attr}" '
            f'data-ref="{_esc(sid)}" fill="none" />'
        )

    # 5. Extra explicit segments
    for p1_id, p2_id, css_cls in extra_segments or []:
        if p1_id in coords and p2_id in coords:
            p1_s = vp.to_svg(*coords[p1_id])
            p2_s = vp.to_svg(*coords[p2_id])
            d_attr = _three_vertex_path(p1_s[0], p1_s[1], p2_s[0], p2_s[1])
            ref = f"/ {p1_id} {p2_id} /"
            aliases = f"/ {p2_id} {p1_id} / | {p1_id}{p2_id} | {p2_id}{p1_id}"
            graphics_lines.append(
                f'      <path class="geom-segment {css_cls}" d="{d_attr}" '
                f'data-ref="{_esc(ref)}" data-aliases="{_esc(aliases)}" fill="none" />'
            )

    # 6. Golden highlights + interactive overlays
    for hl in golden_segments or []:
        if hl.p1 in coords and hl.p2 in coords:
            p1_s = vp.to_svg(*coords[hl.p1])
            p2_s = vp.to_svg(*coords[hl.p2])
            d_attr = _three_vertex_path(p1_s[0], p1_s[1], p2_s[0], p2_s[1])
            ref = f"/ {hl.p1} {hl.p2} /"
            aliases = f"/ {hl.p2} {hl.p1} / | {hl.p1}{hl.p2} | {hl.p2}{hl.p1}"
            if hl.role == "golden-major":
                graphics_lines.append(
                    f'      <path class="geom-segment golden-major-glow" d="{d_attr}" fill="none" />'
                )
            graphics_lines.append(
                f'      <path class="geom-segment {hl.role}" d="{d_attr}" '
                f'data-ref="{_esc(ref)}" data-aliases="{_esc(aliases)}" fill="none" />'
            )
            highlights_lines.append(
                f'      <path class="geom-overlay" d="{d_attr}" '
                f'data-ref="{_esc(ref)}" data-aliases="{_esc(aliases)}" />'
            )

    # 7. Points & labels (placed slightly offset from centroid)
    center_sx = 0.5 * width
    center_sy = 0.5 * height
    points_lines: list[str] = []
    labels_lines: list[str] = []
    for pid, (wx, wy) in coords.items():
        sx, sy = vp.to_svg(wx, wy)
        cls = "geom-point"
        if pid in golden_pts:
            cls += " golden-point"
            points_lines.append(
                f'      <circle class="geom-point-halo" cx="{_fmt(sx)}" cy="{_fmt(sy)}" r="7.5" />'
            )
        elif pid in given_pts:
            cls += " given-point"
        r_pt = "4.4" if pid in golden_pts else "3.6"
        points_lines.append(
            f'      <circle class="{cls}" cx="{_fmt(sx)}" cy="{_fmt(sy)}" r="{r_pt}" '
            f'data-ref="{_esc(pid)}"><title>{_esc(pid)}</title></circle>'
        )
        dx = sx - center_sx
        dy = sy - center_sy
        norm = math.hypot(dx, dy) or 1.0
        lx = max(14.0, min(width - 22.0, sx + 13.0 * (dx / norm)))
        ly = max(18.0, min(height - 10.0, sy + 13.0 * (dy / norm) + 4.0))
        labels_lines.append(
            f'      <text class="geom-label" x="{_fmt(lx)}" y="{_fmt(ly)}" '
            f'text-anchor="middle" data-ref="{_esc(pid)}">{_esc(pid)}</text>'
        )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
        f'viewBox="0 0 {width} {height}" data-graphic-id="{_esc(graphic_id)}" '
        f'role="img" aria-label="{_esc(title)}">',
        f"  <title>{_esc(title)}</title>",
        _TICK_DEFS,
        "  <style>",
        EMBEDDED_SVG_STYLE,
        "  </style>",
        f'  <rect class="svg-bg" x="0" y="0" width="{width}" height="{height}" rx="6" fill="none" />',
        '  <g id="elements">',
        '    <g id="graphics">',
        *graphics_lines,
        "    </g>",
        '    <g id="highlights" style="pointer-events: none;">',
        *highlights_lines,
        "    </g>",
        '    <g id="points">',
        *points_lines,
        "    </g>",
        '    <g id="labels">',
        *labels_lines,
        "    </g>",
        "  </g>",
        "</svg>",
    ]
    return "\n".join(parts) + "\n"


def export_svg(svg_markup: str, target: Path) -> Path:
    """Write ``svg_markup`` to ``target``, creating parent directories if needed."""
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(svg_markup, encoding="utf-8")
    return target
