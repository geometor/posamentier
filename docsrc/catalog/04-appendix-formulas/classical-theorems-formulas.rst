:type: formula
:order: 4
:excerpt: Exact formulas for Ceva, Menelaus, Stewart, Ptolemy, Brahmagupta, Parameshvara, Morley, Kepler's triangle, and the Golden Cuboid.

Appendix D · Classical Geometric Theorems & Solids
==================================================

**Cross-Links:** :ref:`etc:1stmorleytaylormarrcenter` · :ref:`Euclid III.22 <elements:iii.22>` · :ref:`Euclid VI.3 <elements:vi.3>`

.. list-table:: Exact Classical Theorem & Polyhedral Formulas
   :header-rows: 1
   :widths: 26 46 28

   * - Theorem / Figure
     - Exact Formula
     - Verifier / Reference
   * - Ceva's Theorem
     - :math:`\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = +1`
     - Cevian concurrency
   * - Menelaus's Theorem
     - :math:`\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = -1`
     - Transversal collinearity
   * - Stewart's Theorem
     - :math:`b^2 m + c^2 n = a(d^2 + mn)`
     - :func:`~geometor.posamentier.formulas.verify_stewart_theorem`
   * - Ptolemy's Theorems
     - :math:`ac + bd = ef, \qquad \frac{e}{f} = \frac{ad+bc}{ab+cd}`
     - :func:`~geometor.posamentier.formulas.verify_ptolemy_cyclic_quad`
   * - Brahmagupta's Area
     - :math:`K = \sqrt{(s-a)(s-b)(s-c)(s-d)}`
     - :func:`~geometor.posamentier.formulas.verify_brahmagupta_area`
   * - Parameshvara's Circumradius
     - :math:`R = \frac{1}{4K}\sqrt{(ab+cd)(ac+bd)(ad+bc)}`
     - Cyclic quadrilateral
   * - Morley's Trisector Side
     - :math:`s_{\text{Morley}} = 8R \sin\frac{A}{3} \sin\frac{B}{3} \sin\frac{C}{3}`
     - :func:`~geometor.posamentier.formulas.verify_morley_trisector_side`
   * - Kepler's Triangle
     - :math:`1^2 + (\sqrt{\phi})^2 = \phi^2`
     - :func:`~geometor.posamentier.formulas.verify_kepler_triangle`
   * - Golden Cuboid (:math:`1 \times \phi \times \phi^2`)
     - :math:`d = 2\phi, \quad V = \phi^3, \quad S = 4\phi^3`
     - :func:`~geometor.posamentier.formulas.verify_golden_cuboid`
   * - Regular Icosahedron Vertices
     - :math:`(0, \pm 1, \pm\phi), \; (\pm 1, \pm\phi, 0), \; (\pm\phi, 0, \pm 1)`
     - Edge :math:`= 2`, circumradius :math:`= \sqrt{\phi + 2}`
