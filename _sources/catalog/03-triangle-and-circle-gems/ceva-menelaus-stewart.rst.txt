:type: theorem
:order: 2
:excerpt: Ceva's concurrency theorem, Menelaus's collinearity theorem, Stewart's cevian length theorem, and the Angle Bisector Theorem.

Ceva, Menelaus, Stewart & Angle Bisectors
=========================================

**Cross-Links:** :ref:`Euclid VI.3 <elements:vi.3>` · :ref:`Euclid I.47 <elements:i.47>` · :func:`~geometor.posamentier.formulas.verify_stewart_theorem`

1. **Ceva's Theorem (Cevian Concurrency)**:
   Given points :math:`D \in BC`, :math:`E \in CA`, :math:`F \in AB` on the sidelines of :math:`\triangle ABC`, the cevians :math:`AD, BE, CF` are concurrent (or parallel) if and only if the signed ratio product satisfies:

   .. math::

      \frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = +1.

   Special cases include medians (:math:`X(2)`), internal angle bisectors (:math:`X(1)` via :ref:`Euclid VI.3 <elements:vi.3>`), altitudes (:math:`X(4)`), Gergonne point (:math:`X(7)`), and Nagel point (:math:`X(8)`).

2. **Menelaus's Theorem (Transversal Collinearity)**:
   Points :math:`D \in BC`, :math:`E \in CA`, :math:`F \in AB` (not vertices) are collinear on a transversal line if and only if the signed ratio product satisfies:

   .. math::

      \frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = -1.

3. **Stewart's Theorem (Cevian Length)**:
   If a cevian :math:`AD` of length :math:`d` divides side :math:`BC = a` into segments :math:`BD = m` and :math:`DC = n` (:math:`m + n = a`), then:

   .. math::

      b^2 m + c^2 n = a(d^2 + mn).

   Setting :math:`m = n = a/2` yields Apollonius's median length :math:`m_a = \frac{1}{2}\sqrt{2b^2 + 2c^2 - a^2}`; setting :math:`m/n = c/b` yields the internal angle bisector length :math:`w_a = \frac{2bc}{b+c}\cos\frac{A}{2} = \sqrt{bc\left(1 - \frac{a^2}{(b+c)^2}\right)}`.
