:type: formula
:order: 3
:excerpt: Exact formulas for Heron area, inradius, circumradius, exradii, Euler OI^2, Nine-Point Circle, medians, angle bisectors, and ETC coordinates.

Appendix C · Triangle Centers, Areas & Circles
==============================================

**Cross-Links:** :doc:`Incenter X(1) <etc:centers/c-00001-00019/x-00001/index>` · :doc:`Centroid X(2) <etc:centers/c-00001-00019/x-00002/index>` · :doc:`Circumcenter X(3) <etc:centers/c-00001-00019/x-00003/index>` · :doc:`Orthocenter X(4) <etc:centers/c-00001-00019/x-00004/index>` · :doc:`Nine-Point Center X(5) <etc:centers/c-00001-00019/x-00005/index>`

Let :math:`\triangle ABC` have side lengths :math:`a, b, c`, semiperimeter :math:`s = \frac{a+b+c}{2}`, and area :math:`K`.

.. list-table:: Exact Triangle & Circle Formulas
   :header-rows: 1
   :widths: 26 46 28

   * - Quantity
     - Exact Formula
     - Verifier / Reference
   * - Heron's Area
     - :math:`K = \sqrt{s(s-a)(s-b)(s-c)}`
     - :func:`~geometor.posamentier.formulas.verify_heron_and_inradius`
   * - Inradius (:math:`r`) & Exradii (:math:`r_a`)
     - :math:`r = \frac{K}{s}, \qquad r_a = \frac{K}{s - a}`
     - :math:`K = \sqrt{r \, r_a \, r_b \, r_c}`
   * - Circumradius (:math:`R`)
     - :math:`R = \frac{abc}{4K} = \frac{a}{2\sin A}`
     - :ref:`Euclid IV.5 <elements:iv.5>`
   * - Nine-Point Circle Radius (:math:`R_9`)
     - :math:`R_9 = \frac{R}{2}`
     - Tangent to incircle & excircles
   * - Euler's :math:`OI^2` Formula
     - :math:`OI^2 = R(R - 2r)`
     - :func:`~geometor.posamentier.formulas.verify_euler_oi_distance`
   * - Euler Line Ratios
     - :math:`OG : GN_9 : N_9 H = 2 : 1 : 3, \qquad OH = 3\,OG`
     - :math:`O = X(3), G = X(2), N_9 = X(5), H = X(4)`
   * - Median Length (:math:`m_a`)
     - :math:`m_a = \frac{1}{2}\sqrt{2b^2 + 2c^2 - a^2}`
     - :math:`m_a^2 + m_b^2 + m_c^2 = \frac{3}{4}(a^2+b^2+c^2)`
   * - Angle Bisector Length (:math:`w_a`)
     - :math:`w_a = \frac{2bc}{b+c}\cos\frac{A}{2} = \sqrt{bc\left(1 - \frac{a^2}{(b+c)^2}\right)}`
     - :ref:`Euclid VI.3 <elements:vi.3>`
   * - Barycentric Coordinates
     - :math:`X(1) = (a:b:c), \; X(2) = (1:1:1), \; X(3) = (a^2(b^2+c^2-a^2):\dots)`
     - Cross-linked to ``geometor/etc``
