:type: fact
:order: 2
:excerpt: Exact algebraic identities of phi, power linearization, continued fractions, Binet/Lucas/Cassini identities, Millin series, and 18/36-degree radicals.

Numerical Value & Algebraic Properties (Ch. 3)
==============================================

**Source Locus:** Chapter 3 (pp. 49–80 · Proofs pp. 305–311) · **Verifier:** :mod:`geometor.posamentier.formulas`

.. enunciation::

   The golden ratio :math:`\phi = \frac{1 + \sqrt{5}}{2}` is the unique positive root of :math:`x^2 - x - 1 = 0`. Every integer power :math:`\phi^n` linearizes over :math:`\mathbb{Q}(\phi)` via Fibonacci coefficients: :math:`\phi^n = F_n \phi + F_{n-1}`.

Key Algebraic & Number-Theoretic Facts
--------------------------------------

1. **Continued Fraction & Nested Radical**:

   .. math::

      \phi = [1; 1, 1, 1, \dots] = 1 + \cfrac{1}{1 + \cfrac{1}{1 + \ddots}} = \sqrt{1 + \sqrt{1 + \sqrt{1 + \cdots}}}

   The partial convergents are successive Fibonacci ratios :math:`F_{n+1}/F_n`, alternating above and below :math:`\phi`. By Hurwitz's theorem, :math:`\phi` is the most poorly approximable irrational number (:math:`|\phi - p/q| > 1/(\sqrt{5}\,q^2)`).

2. **Power Linearization & Conjugate**:
   Let :math:`\psi = 1 - \phi = -1/\phi = \frac{1-\sqrt{5}}{2}`. Both :math:`\phi` and :math:`\psi` satisfy :math:`x^2 = x + 1`, whence induction yields (:func:`~geometor.posamentier.formulas.verify_phi_power_linearization`):

   .. math::

      \phi^n = F_n \phi + F_{n-1}, \qquad \psi^n = F_n \psi + F_{n-1}, \qquad \phi^{-n} = (-1)^n \left(F_{n-1} - F_n \psi\right).

3. **Binet, Lucas & Cassini Identities**:

   .. math::

      F_n = \frac{\phi^n - \psi^n}{\sqrt{5}}, \qquad L_n = \phi^n + \psi^n, \qquad F_{n+1}F_{n-1} - F_n^2 = (-1)^n.

4. **Millin Series (Reciprocal Fermat-Indexed Fibonacci Sum)**:

   .. math::

      \sum_{k=0}^{\infty} \frac{1}{F_{2^k}} = \frac{7 - \sqrt{5}}{2} = 4 - \phi.

5. **Exact Pentagonal Trigonometry** (:func:`~geometor.posamentier.formulas.verify_pentagonal_trig`):

   .. math::

      \sin 18^\circ = \cos 72^\circ = \frac{\sqrt{5}-1}{4} = \frac{1}{2\phi}, \qquad \cos 36^\circ = \sin 54^\circ = \frac{1+\sqrt{5}}{4} = \frac{\phi}{2}.
