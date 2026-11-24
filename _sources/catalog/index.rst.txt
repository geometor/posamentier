:navigation: header
:order: 1
:type: book
:nav_title: Mathematical Catalog
:breadcrumb_title: Mathematical Catalog
:layout: book
:book_title: The Glorious Golden Ratio — Mathematical Catalog & Concordance
:author: Alfred S. Posamentier & Ingmar Lehmann · Exact Synthesis by GEOMETOR
:year: 2011
:edition_year: 2026
:excerpt: An exact symbolic mathematical catalog, Euclidean construction taxonomy, geometric facts, and Appendix of Formulas inspired by Posamentier & Lehmann's The Glorious Golden Ratio.

.. _posamentier-catalog:

====================
Mathematical Catalog
====================

.. rubric:: Atomic Golden-Ratio Constructions, Geometric Facts, Appendix of Formulas & Cross-Corpus Equivalences

.. container:: title-page

   | **Reference Corpus:** *The Glorious Golden Ratio* (Prometheus Books, 2011/2012, ISBN ``978-1-61614-423-4``) & Triangle/Circle Geometry Treatises
   | **Authors:** :person:`Alfred S. Posamentier <posamentier>` & :person:`Ingmar Lehmann <lehmann>` *(Ch. 7 on Fractals by :person:`Ana Lúcia Braz Dias <dias>`)*
   | **Digital Synthesis:** GEOMETOR (100% Exact ``SymPy`` Algebra, ``geometor.model`` Constructions & Equivalence Triage)

This catalog synthesizes the atomic mathematical claims, Euclidean constructions, geometric facts, and algebraic identities inspired by *The Glorious Golden Ratio* and Posamentier's triangle and circle geometry monographs, pairing each theorem with original GEOMETOR mathematical prose, exact symbolic formulations over :math:`\mathbb{Q}(\phi)`, calibrated ``.euclid-graphic`` vector plates, and cross-corpus links to :ref:`elements <elements:ii.11>` and ``geometor/etc``.

Collections
-----------

.. collection::
   :type: collection
   :sort: order

Chapter Architecture
--------------------

1. **Ch. 1 — Defining and Constructing the Golden Ratio** *(pp. 13–38 · Proofs pp. 295–304)*: 16 numbered straightedge-and-compass and Mascheroni circle constructions (``POS-1.01``–``POS-1.16``).
2. **Ch. 2 — History of the Golden Ratio** *(pp. 39–48)*: Kepler's :math:`1 : \sqrt{\phi} : \phi` triangle, Euclid, Fibonacci, Pacioli, Ohm, Zeising, and exact-vs-approximate historical residual audit.
3. **Ch. 3 — Numerical Value & Algebraic Properties** *(pp. 49–80 · Proofs pp. 305–311)*: :math:`\phi^n = F_n \phi + F_{n-1}`, continued fraction ``[1; 1, 1, ...]``, nested radicals, Binet/Lucas/Cassini identities, Millin series, and :math:`18^\circ / 36^\circ` radicals.
4. **Ch. 4 — Golden Geometric Figures** *(pp. 81–190 · Proofs pp. 312–325)*: Whirling-square rectangles, semicircle-on-side square section (``POS-4.01``), golden triangles & gnomons, folded paper-strip pentagon knot (``POS-4.02``), Golden Ellipse, Golden Cuboid :math:`1 \times \phi \times \phi^2` (``POS-4.03``), and icosahedron/dodecahedron coordinates.
5. **Ch. 5 — Unexpected Appearances** *(pp. 191–246 · Proofs pp. 326–330)*: Star of David hexagram :math:`\phi` chord section (``POS-5.01``), similar triangles on reference-triangle sides, ``64 = 65`` Cassini dissection, Pascal shallow diagonals, and random-walk stopping probability :math:`1/\phi`.
6. **Ch. 6 — The Plant Kingdom** *(pp. 247–268)*: Phyllotaxis parastichies and the Golden Angle :math:`360^\circ / \phi^2` (cross-linked to ``geometor/phyllotaxis``).
7. **Ch. 7 — Fractals and the Golden Ratio** *(pp. 269–292 · Proofs pp. 331–332, by Ana Lúcia Braz Dias)*: Symmetric Golden Fractal Tree :math:`r = 1/\phi` (``POS-7.01``) and Sierpiński-Pentagon :math:`r = 1/\phi^2` (``POS-7.02``).

Chapter 1 — 16 Constructions Equivalence Matrix
-----------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 12 36 16 18 18

   * - ID
     - Construction Locus
     - Relation
     - ``divine`` / ``knott`` / ``huntley``
     - Underlying Identity
   * - :doc:`01-constructions/pos-1-01`
     - Square ``ABCD``, midpoint ``M`` of ``AD``, arc ``MB``
     - **Equivalent**
     - ``GC-01.01`` · ``KNOTT-1.1`` · ``HUNT-02.01``
     - :ref:`Euclid II.11 <elements:ii.11>` (:math:`1:2:\sqrt{5}` leg extension)
   * - :doc:`01-constructions/pos-1-02`
     - :math:`1:2:\sqrt{5}` right-triangle hypotenuse arc transfer
     - **Equivalent**
     - ``GC-01.02`` · ``KNOTT-1.1`` · ``HUNT-02.02``
     - :ref:`Euclid VI.30 <elements:vi.30>` secant transfer
   * - :doc:`01-constructions/pos-1-03`
     - :math:`1 \times 3` three-square grid + angle bisector
     - **Net-New**
     - Cousin of ``GC-03.04``
     - :ref:`Euclid VI.3 <elements:vi.3>` angle-bisector ratio
   * - :doc:`01-constructions/pos-1-04`
     - :math:`1 \times 2` double-square shared-midpoint circle on diagonal
     - **Variant**
     - ``GC-03.01`` · ``KNOTT-1.2``
     - Circle secant on :math:`\sqrt{5}` diagonal
   * - :doc:`01-constructions/pos-1-05`
     - Unit square + semicircle on extended side through vertex
     - **Variant**
     - ``GC-01.01``
     - Thales right-triangle mean proportional
   * - :doc:`01-constructions/pos-1-06`
     - George Odom's inscribed equilateral midline chord
     - **Equivalent**
     - ``GC-02.01``
     - :ref:`Intersecting Chords (III.35) <elements:iii.35>`
   * - :doc:`01-constructions/pos-1-07`
     - :math:`2:\sqrt{5}:\sqrt{5}` isosceles incircle (:math:`r = 1/\phi`)
     - **Net-New**
     - Cousin of ``GC-03.06``
     - Half-angle tangent :math:`\tan(\theta/2) = 1/\phi`
   * - :doc:`01-constructions/pos-1-08`
     - Unit square :math:`\sqrt{2}`-diagonal circle + equilateral hybrid
     - **Net-New**
     - —
     - Quadratic circle–circle radical locus
   * - :doc:`01-constructions/pos-1-09`
     - Circle unit chord ``AB`` & equal external tangent ``PT``
     - **Net-New**
     - Dual of ``GC-06.01``
     - :ref:`Tangent–Secant Power (III.36) <elements:iii.36>`
   * - :doc:`01-constructions/pos-1-10`
     - Huntley's ``3–4–5`` right-triangle angle bisector circle
     - **Equivalent**
     - ``GC-04.01`` · ``HUNT-03.01``
     - ``3–4–5`` half-angle tangent :math:`1/2 \implies \sqrt{5}`
   * - :doc:`01-constructions/pos-1-11`
     - Three concentric circles (:math:`r = 1, 2, 4`) secant–tangent
     - **Variant**
     - ``GC-06.02``
     - Power-of-point radial scaling
   * - :doc:`01-constructions/pos-1-12`
     - Three adjacent congruent unit circles outer secant
     - **Variant**
     - ``GC-06.04``
     - :math:`1:2:\sqrt{5}` center-line transversal
   * - :doc:`01-constructions/pos-1-13`
     - Three mutually tangent circles inside a semicircle
     - **Equivalent**
     - ``GC-06.07``
     - Descartes / Soddy Sangaku quadratic
   * - :doc:`01-constructions/pos-1-14`
     - Hans Walser's coordinate-grid circles (:math:`r = 1, 3`)
     - **Net-New**
     - —
     - Radical-axis Cartesian intersection
   * - :doc:`01-constructions/pos-1-15`
     - Right-triangle two-arc radical-leg difference
     - **Variant**
     - ``GC-01.02`` · ``HUNT-02.02``
     - :math:`1:2:\sqrt{5}` difference of arcs
   * - :doc:`01-constructions/pos-1-16`
     - Kurt Hofstetter's 5-circle compass-only construction
     - **Equivalent**
     - ``GC-01.05``
     - Mascheroni symmetric circle locus

.. toctree::
   :hidden:

   01-constructions/index
   02-golden-figures-and-facts/index
   03-triangle-and-circle-gems/index
   04-appendix-formulas/index
