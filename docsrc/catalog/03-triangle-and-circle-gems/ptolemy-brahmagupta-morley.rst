:type: theorem
:order: 3
:excerpt: Ptolemy's First and Second Theorems, Brahmagupta's cyclic quadrilateral area, Parameshvara's circumradius, and Morley's Trisector Theorem.

Ptolemy, Brahmagupta & Morley's Trisector Theorem
=================================================

**Cross-Links:** :ref:`etc:1stmorleytaylormarrcenter` · :ref:`Euclid III.22 <elements:iii.22>` · :func:`~geometor.posamentier.formulas.verify_ptolemy_cyclic_quad`

1. **Ptolemy's First & Second Theorems (Cyclic Quadrilaterals)**:
   For a convex quadrilateral :math:`ABCD` with consecutive sides :math:`a, b, c, d` and diagonals :math:`e = AC`, :math:`f = BD`, Ptolemy's inequality :math:`ac + bd \ge ef` holds with equality if and only if :math:`ABCD` is cyclic:

   .. math::

      ac + bd = ef, \qquad \frac{e}{f} = \frac{ad + bc}{ab + cd}.

2. **Brahmagupta's Formula & Parameshvara's Circumradius**:
   For a cyclic quadrilateral with sides :math:`a, b, c, d` and semiperimeter :math:`s = \frac{a+b+c+d}{2}`, the exact area :math:`K` and circumradius :math:`R` are (:func:`~geometor.posamentier.formulas.verify_brahmagupta_area`):

   .. math::

      K = \sqrt{(s-a)(s-b)(s-c)(s-d)}, \qquad R = \frac{1}{4K}\sqrt{(ab+cd)(ac+bd)(ad+bc)}.

   Setting :math:`d = 0` recovers Heron's triangle area formula and :math:`R = \frac{abc}{4K}`.

3. **Morley's Trisector Theorem**:
   In any triangle :math:`\triangle ABC`, the three points of intersection of the adjacent internal angle trisectors form an **equilateral triangle** (Morley's triangle) whose side length is (:func:`~geometor.posamentier.formulas.verify_morley_trisector_side`):

   .. math::

      s_{\text{Morley}} = 8R \sin\frac{A}{3} \sin\frac{B}{3} \sin\frac{C}{3}.

   The first Morley–Taylor–Marr center is cataloged in ``geometor/etc`` as :ref:`etc:1stmorleytaylormarrcenter`.
