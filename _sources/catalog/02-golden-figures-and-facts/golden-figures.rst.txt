:type: fact
:order: 3
:excerpt: Golden rectangles, whirling squares, POS-4.01 semicircle square section, golden triangles/gnomons, paper-knot pentagon, golden ellipse, and Golden Cuboid.

Golden Geometric Figures (Ch. 4)
================================

**Source Locus:** Chapter 4 (pp. 81–190 · Proofs pp. 312–325) · **Cross-Links:** :ref:`Euclid IV.10–11 <elements:iv.10>`, ``geometor/polyhedra``

1. **Whirling-Square Golden Rectangles**:
   A rectangle of aspect ratio :math:`\phi : 1` is self-similar under gnomonic dissection: removing a :math:`1 \times 1` square leaves a :math:`1 \times (\phi - 1) = 1 \times \frac{1}{\phi}` golden rectangle. Iterating this dissection produces a nested sequence of squares whose quarter-circle arcs approximate the logarithmic golden spiral :math:`r(\theta) = r_0 \phi^{2\theta/\pi}`.

2. **POS-4.01 · Semicircle on Square Side Cutting Midpoint-Diagonal in Golden Ratio**:

   .. picture:: pos-4-01.svg
      :alt: POS-4.01 — Semicircle on Square Side Cutting Midpoint-Diagonal

   In square :g:`ABCD` of side :math:`2` with base midpoint :g:`M` :math:`=(1,0)`, the semicircle :g:`cM` of radius :math:`1` cuts the midpoint-diagonal :g:`DM` (length :math:`\sqrt{5}`) at :g:`P` and extends to :g:`E`. Since :math:`|DP| = \sqrt{5} - 1 = 2/\phi` and diameter :math:`|PE| = 2`, the ratio :g:`PE` / :g:`DP` equals :math:`\phi` (:func:`~geometor.posamentier.constructions.build_pos_4_01`).

3. **Golden Triangles & Golden Gnomons** (:ref:`Euclid IV.10 <elements:iv.10>`):
   - **Acute Golden Triangle** (:math:`72^\circ\text{–}72^\circ\text{–}36^\circ`): Leg-to-base ratio :math:`\phi : 1`. Bisecting a base angle partitions it into a smaller :math:`72^\circ\text{–}72^\circ\text{–}36^\circ` triangle and an obtuse golden gnomon.
   - **Obtuse Golden Gnomon** (:math:`36^\circ\text{–}36^\circ\text{–}108^\circ`): Base-to-leg ratio :math:`\phi : 1`. Every regular pentagon and pentagram decomposes exclusively into these two triangles.

4. **POS-4.02 · Folded Paper-Strip Overhand Knot Regular Pentagon**:
   Tying a flat overhand knot in a uniform-width paper strip of width :math:`w` and creasing it flat produces a regular pentagon of side :math:`s = w / \sin 72^\circ = \frac{4w}{\sqrt{10 + 2\sqrt{5}}}` and diagonal-to-side ratio :math:`\phi`.

5. **The Golden Ellipse**:
   An ellipse with semi-major axis :math:`a` and semi-minor axis :math:`b` satisfying :math:`a / b = \phi` has eccentricity :math:`e = \sqrt{1 - 1/\phi^2} = 1/\sqrt{\phi}` and focal ratios :math:`c/b = \sqrt{\phi}` and :math:`a/c = \sqrt{\phi}` (since :math:`c^2 = a^2 - b^2 = b^2(\phi^2 - 1) = b^2\phi`).

6. **POS-4.03 · The Golden Cuboid** (:math:`1 \times \phi \times \phi^2`) **& Platonic Solids**:
   A rectangular box with edge lengths :math:`1, \phi, \phi^2` has space diagonal :math:`d = \sqrt{1 + \phi^2 + \phi^4} = \sqrt{4\phi^2} = 2\phi` (:func:`~geometor.posamentier.formulas.verify_golden_cuboid`), volume :math:`V = \phi^3`, and surface area :math:`S = 2(\phi + \phi^2 + \phi^3) = 4\phi^3`. In 3D, three mutually orthogonal golden rectangles form the 12 vertices of a regular icosahedron, :math:`(\pm 1, \pm \phi, 0)` and cyclic permutations.
