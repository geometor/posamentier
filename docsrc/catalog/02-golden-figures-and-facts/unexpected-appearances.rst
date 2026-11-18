:type: fact
:order: 4
:excerpt: Star of David hexagram golden chord section (POS-5.01), similar triangles on triangle sides, 64=65 Cassini dissection, Pascal shallow diagonals, and random walks.

Unexpected Appearances of the Golden Ratio (Ch. 5)
==================================================

**Source Locus:** Chapter 5 (pp. 191–246 · Proofs pp. 326–330)

1. **POS-5.01 · Star of David Hexagram Inscribed Circle Golden Chord Section**:

   .. picture:: pos-5-01.svg
      :alt: POS-5.01 — Star of David Hexagram Inscribed Circle Golden Chord Section

   In a regular hexagram formed by two congruent equilateral triangles :g:`ABC` and :g:`A1B1C1` inscribed in circle :g:`cO` of radius :math:`2`, the midline :g:`MN` of :g:`ABC` extended to :g:`cO` at :g:`P` satisfies :math:`|MN|/|NP| = \phi` (:func:`~geometor.posamentier.constructions.build_pos_5_01`).

2. **The ``64 = 65`` Cassini Dissection Paradox**:
   By Cassini's identity :math:`F_{n+1} F_{n-1} - F_n^2 = (-1)^n`, an :math:`8 \times 8` square (area :math:`64 = F_6^2`) dissected into two :math:`3 \times 8` right triangles and two :math:`(3, 5) \times 5` trapezoids reassembles into an apparent :math:`5 \times 13` rectangle (area :math:`65 = F_5 F_7`), hiding a thin parallelogram gap of area :math:`1` along the diagonal because the slopes :math:`3/8` and :math:`2/5` differ by :math:`1/40`.

3. **Pascal's Triangle Shallow Diagonals**:
   Summing along shallow diagonals of Pascal's triangle recovers the Fibonacci numbers:

   .. math::

      F_{n+1} = \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n-k}{k}, \qquad \lim_{n\to\infty} \frac{F_{n+1}}{F_n} = \phi.

4. **Random-Walk & Gambler's Ruin Stopping Probability**:
   A fair-coin walk starting at :math:`1` with absorbing barriers at :math:`0` and :math:`n` or Fibonacci-biased transition thresholds yields hitting probabilities governed by :math:`1/\phi` in golden-ratio step-size martingales.
