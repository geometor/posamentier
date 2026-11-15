:navigation: header
:order: 10

=====
About
=====

``geometor.posamentier`` is developed and maintained by **phiarchitect** as part of the **GEOMETOR** organization.

Exact symbolic mathematical catalog and concordance inspired by The Glorious Golden Ratio (Alfred S. Posamentier & Ingmar Lehmann)

Repository Architecture
-----------------------

- **Python Package**: ``src/geometor/posamentier/`` (Python 3.13)
- **Mathematical Catalog**: ``docsrc/catalog/`` (``:layout: book``)
- **Manifest & Concordance**: ``resources/catalog_manifest.json``, ``resources/concordance.json``
- **Automated Verification**: ``tests/`` (``pytest`` + ``ruff``) and ``docsrc/`` (``publish build``)
