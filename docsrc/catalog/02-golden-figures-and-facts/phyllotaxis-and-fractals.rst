:type: fact
:order: 5
:excerpt: Golden Angle phyllotaxis (Ch. 6) and self-similar Golden Fractal Tree and Sierpinski-Pentagon scaling factors (Ch. 7).

The Plant Kingdom & Golden Fractals (Ch. 6 & Ch. 7)
===================================================

**Source Locus:** Chapter 6 (pp. 247–268) & Chapter 7 (pp. 269–292 · Proofs pp. 331–332, by :person:`Ana Lúcia Braz Dias <dias>`)

1. **Botanical Phyllotaxis & The Golden Angle (Ch. 6)**:
   Successive primordia in sunflower capitula, pinecones, and spiral phyllotaxis diverge by the **Golden Angle**:

   .. math::

      \theta_\phi = \frac{360^\circ}{\phi^2} = 360^\circ(2 - \phi) \approx 137.50776^\circ \quad \left(\text{complement } \frac{360^\circ}{\phi} \approx 222.49224^\circ\right).

   Because :math:`\phi` has the slowest-converging continued fraction ``[1; 1, 1, ...]``, this divergence minimizes radial overlap and produces visible parastichy spiral counts in consecutive Fibonacci pairs :math:`(F_k, F_{k+1})` (cross-linked to ``geometor/phyllotaxis``).

2. **POS-7.01 · Symmetric Binary Golden Fractal Tree** (:math:`r = 1/\phi`):
   A symmetric binary tree with branching angle :math:`\theta = 60^\circ` (or :math:`45^\circ`–:math:`90^\circ` variants) and branch contraction factor :math:`r` achieves exact self-contact of its limiting canopy when the geometric series :math:`\sum_{k=1}^{\infty} r^k = \frac{r}{1-r}` matches the unit trunk, i.e. :math:`r^2 + r - 1 = 0 \implies r = \frac{1}{\phi} = \phi - 1`.

3. **POS-7.02 · Non-Overlapping Sierpiński-Pentagon** (:math:`r = 1/\phi^2`):
   Replacing a regular pentagon with five corner-touching scaled copies of ratio :math:`r` without overlap requires two adjacent scaled pentagons along a unit base to touch at a vertex when :math:`r + r\phi = 1 \implies r(1 + \phi) = 1 \implies r = \frac{1}{\phi^2} = \frac{3 - \sqrt{5}}{2}`. Its Hausdorff similarity dimension is:

   .. math::

      D_H = \frac{\ln 5}{\ln(\phi^2)} = \frac{\ln 5}{2 \ln \phi} \approx 1.67228.
