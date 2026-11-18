:type: theorem
:order: 1
:excerpt: Euler line, Nine-Point Circle, Feuerbach's theorem, Simson line, and triangle centers X(1)–X(6) cross-linked to geometor/etc.

Triangle Centers, Euler Line & Nine-Point Circle
=================================================

**Cross-Links:** :doc:`Incenter X(1) <etc:centers/c-00001-00019/x-00001/index>` · :doc:`Centroid X(2) <etc:centers/c-00001-00019/x-00002/index>` · :doc:`Circumcenter X(3) <etc:centers/c-00001-00019/x-00003/index>` · :doc:`Orthocenter X(4) <etc:centers/c-00001-00019/x-00004/index>` · :doc:`Nine-Point Center X(5) <etc:centers/c-00001-00019/x-00005/index>` · :doc:`Symmedian Point X(6) <etc:centers/c-00001-00019/x-00006/index>`

.. enunciation::

   In any non-equilateral triangle :g:`ABC`, the circumcenter :g:`O`, centroid :g:`G`, nine-point center :g:`N9`, and orthocenter :g:`H` are collinear on the **Euler line**, satisfying :math:`OG : GN_9 : N_9 H = 2 : 1 : 3` and :math:`OH = 3 \cdot OG`.

.. picture:: euler-nine-point.svg
   :alt: Euler Line and Nine-Point Circle on the 13-14-15 Heron Triangle

Exact 13–14–15 Heron Witness
----------------------------

For :g:`A` :math:`=(0,0)`, :g:`B` :math:`=(14,0)`, :g:`C` :math:`=(5,12)` (sides :math:`a=13, b=15, c=14`, area :math:`K=84`, semiperimeter :math:`s=21`):

- **Incenter** :g:`I` (:doc:`X(1) <etc:centers/c-00001-00019/x-00001/index>`): :math:`(6, 4)`, inradius :math:`r = K/s = 4` (:ref:`Euclid IV.4 <elements:iv.4>`).
- **Centroid** :g:`G` (:doc:`X(2) <etc:centers/c-00001-00019/x-00002/index>`): :math:`(19/3, 4)`.
- **Circumcenter** :g:`O` (:doc:`X(3) <etc:centers/c-00001-00019/x-00003/index>`): :math:`(7, 33/8)`, circumradius :math:`R = abc/(4K) = 65/8` (:ref:`Euclid IV.5 <elements:iv.5>`).
- **Orthocenter** :g:`H` (:doc:`X(4) <etc:centers/c-00001-00019/x-00004/index>`): :math:`(5, 15/4)`.
- **Nine-Point Center** :g:`N9` (:doc:`X(5) <etc:centers/c-00001-00019/x-00005/index>`): :math:`(6, 63/16)`, nine-point radius :math:`R_9 = R/2 = 65/16`.

Key Circle & Line Theorems
--------------------------

1. **Nine-Point Circle**: Passes through the 3 side midpoints, the 3 altitude feet, and the 3 midpoints between :g:`H` and vertices :g:`A, B, C`.
2. **Feuerbach's Theorem**: The Nine-Point Circle is internally tangent to the incircle and externally tangent to all three excircles.
3. **Euler's Distance Formula**: :math:`OI^2 = R(R - 2r)`, whence :math:`R \ge 2r` with equality iff :math:`\triangle ABC` is equilateral (:func:`~geometor.posamentier.formulas.verify_euler_oi_distance`).
4. **Simson–Wallace Line**: The feet of the perpendiculars dropped from a point :math:`P` to the sidelines of :math:`\triangle ABC` are collinear if and only if :math:`P` lies on the circumcircle :g:`cO`.
