:type: formula
:order: 1
:excerpt: Exact algebraic, radical, continued-fraction, power-linearization, and pentagonal trigonometric/spread formulas for phi.

Appendix A · Golden Ratio Formulas (:math:`\phi`)
=================================================

**Symbolic Verifier:** :mod:`geometor.posamentier.formulas`

.. list-table:: Exact Golden Ratio Identities
   :header-rows: 1
   :widths: 28 42 30

   * - Identity
     - Exact Formula
     - SymPy / Algebraic Form
   * - Defining Quadratic
     - :math:`\phi^2 - \phi - 1 = 0`
     - ``sp.GoldenRatio**2 - sp.GoldenRatio - 1``
   * - Closed Radical & Conjugate
     - :math:`\phi = \frac{1+\sqrt{5}}{2}, \quad \psi = \frac{1-\sqrt{5}}{2} = -\frac{1}{\phi}`
     - ``(1 + sp.sqrt(5)) / 2``
   * - Reciprocal & Square
     - :math:`\frac{1}{\phi} = \phi - 1, \qquad \phi^2 = \phi + 1`
     - ``1 / PHI == PHI - 1``
   * - Power Linearization
     - :math:`\phi^n = F_n \phi + F_{n-1}`
     - :func:`~geometor.posamentier.formulas.verify_phi_power_linearization`
   * - Negative Powers
     - :math:`\phi^{-n} = (-1)^n \left(F_{n+1} - F_n \phi\right)`
     - Alternating sign in :math:`\mathbb{Z}[\phi]`
   * - Continued Fraction
     - :math:`\phi = [1; 1, 1, 1, \dots]`
     - Convergents :math:`F_{n+1}/F_n`
   * - Nested Radical
     - :math:`\phi = \sqrt{1 + \sqrt{1 + \sqrt{1 + \cdots}}}`
     - Fixed point of :math:`x \mapsto \sqrt{1+x}`
   * - Golden Angle
     - :math:`\theta_\phi = \frac{360^\circ}{\phi^2} = 360^\circ(2 - \phi)`
     - Radians: :math:`2\pi / \phi^2`
   * - Pentagonal Sines & Cosines
     - :math:`\sin 18^\circ = \frac{1}{2\phi}, \quad \cos 36^\circ = \frac{\phi}{2}`
     - :func:`~geometor.posamentier.formulas.verify_pentagonal_trig`
   * - Rational Trig Spreads
     - :math:`s(18^\circ) = \frac{3-\sqrt{5}}{8} = \frac{1}{4\phi^2}, \quad s(36^\circ) = \frac{5-\sqrt{5}}{8}`
     - Exact over :math:`\mathbb{Q}(\phi)`
