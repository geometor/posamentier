:type: formula
:order: 2
:excerpt: Exact Binet, Lucas, Cassini, d'Ocagne, Catalan, Vajda, summation, Millin series, and Fibonacci-Pythagorean formulas.

Appendix B · Fibonacci & Lucas Identities
=========================================

**Symbolic Verifier:** :mod:`geometor.posamentier.formulas`

.. list-table:: Exact Fibonacci (:math:`F_n`) and Lucas (:math:`L_n`) Formulas
   :header-rows: 1
   :widths: 28 44 28

   * - Identity
     - Exact Formula
     - Notes / Verifier
   * - Binet's Formula (:math:`F_n`)
     - :math:`F_n = \frac{\phi^n - \psi^n}{\sqrt{5}}`
     - :func:`~geometor.posamentier.formulas.verify_binet_fibonacci`
   * - Binet's Formula (:math:`L_n`)
     - :math:`L_n = \phi^n + \psi^n = F_{n-1} + F_{n+1}`
     - :func:`~geometor.posamentier.formulas.verify_binet_lucas`
   * - Cassini's Identity
     - :math:`F_{n+1} F_{n-1} - F_n^2 = (-1)^n`
     - :func:`~geometor.posamentier.formulas.verify_cassini_identity`
   * - Catalan's Identity
     - :math:`F_n^2 - F_{n-r} F_{n+r} = (-1)^{n-r} F_r^2`
     - Generalizes Cassini (:math:`r=1`)
   * - d'Ocagne's Identity
     - :math:`F_m F_{n+1} - F_{m+1} F_n = (-1)^n F_{m-n}`
     - Addition determinant
   * - Vajda's Identity
     - :math:`F_{n+i} F_{n+j} - F_n F_{n+i+j} = (-1)^n F_i F_j`
     - Unifies Catalan & d'Ocagne
   * - Sum of First :math:`n` Terms
     - :math:`\sum_{k=1}^{n} F_k = F_{n+2} - 1, \qquad \sum_{k=1}^{n} F_k^2 = F_n F_{n+1}`
     - Telescoping & tiling proof
   * - Millin Series
     - :math:`\sum_{k=0}^{\infty} \frac{1}{F_{2^k}} = \frac{7 - \sqrt{5}}{2} = 4 - \phi`
     - Fermat-indexed reciprocals
   * - Fibonacci–Pythagorean Triples
     - :math:`\left(F_n F_{n+3},\; 2 F_{n+1} F_{n+2},\; F_{n+1}^2 + F_{n+2}^2\right)`
     - Satisfies :math:`a^2 + b^2 = c^2`
