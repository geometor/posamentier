:type: fact
:order: 1
:excerpt: Kepler's right triangle (1, sqrt(phi), phi) bridging the Pythagorean Theorem and the Golden Section.

Kepler's Golden Right Triangle (Ch. 2)
======================================

**Historical Locus:** Chapter 2 (pp. 39–48) · **Cross-Links:** :ref:`Euclid I.47 <elements:i.47>`, :ref:`Euclid II.11 <elements:ii.11>`

.. enunciation::

   A right triangle :g:`ABC` has side lengths in geometric progression :math:`1 : \sqrt{\phi} : \phi` if and only if its hypotenuse :g:`AB` is divided by the altitude from :g:`C` in the golden ratio, and its legs satisfy :math:`1^2 + (\sqrt{\phi})^2 = \phi^2`.

.. picture:: kepler-triangle.svg
   :alt: Kepler's Golden Right Triangle 1 : sqrt(phi) : phi

Exact Symbolic Geometry
-----------------------

Place :g:`A` at :math:`(0, 0)` and :g:`B` at :math:`(\phi, 0)` on the diameter of semicircle :g:`cM` centered at :g:`M` :math:`=(\phi/2, 0)`. Erecting the altitude at :math:`x = 1/\phi` meets :g:`cM` at :g:`C` :math:`=\left(\frac{1}{\phi}, \frac{1}{\sqrt{\phi}}\right)`.

- **Leg :g:`AC`**: :math:`|AC|^2 = \frac{1}{\phi^2} + \frac{1}{\phi} = \frac{1 + \phi}{\phi^2} = 1 \implies |AC| = 1`.
- **Leg :g:`BC`**: :math:`|BC|^2 = \left(\phi - \frac{1}{\phi}\right)^2 + \frac{1}{\phi} = 1 + \frac{1}{\phi} = \phi \implies |BC| = \sqrt{\phi}`.
- **Hypotenuse :g:`AB`**: :math:`|AB| = \phi`.

Historical Audit
----------------

- **Johannes Kepler's Two Treasures**: Kepler paired the Pythagorean Theorem (:ref:`Euclid I.47 <elements:i.47>`) and the Golden Section (:ref:`Euclid II.11 <elements:ii.11>`) into this unique right triangle whose sides form a geometric progression (:func:`~geometor.posamentier.formulas.verify_kepler_triangle`).
- **Circle–Square Near-Quadrature**: A circle of radius :math:`r = \sqrt{\phi}` has circumference :math:`2\pi\sqrt{\phi} \approx 7.9923`, within :math:`0.1\%` of the perimeter :math:`4 \times 2 = 8` of a square of side :math:`2`, a classical geometric coincidence rather than an exact quadrature.
