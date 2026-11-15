===========
posamentier
===========

Exact symbolic mathematical catalog and concordance inspired by The Glorious Golden Ratio (Alfred S. Posamentier & Ingmar Lehmann)

Catalog Overview
----------------

- **Reference Work**: *The Glorious Golden Ratio* (Alfred S. Posamentier & Ingmar Lehmann)
- **Catalog Track**: ``docsrc/catalog/`` (``:layout: book``)
- **Symbolic Manifest & Concordance**: ``resources/catalog_manifest.json``, ``resources/concordance.json``
Installation & Verification
---------------------------

Managed with ``uv`` on Python 3.13:

.. code-block:: bash

   uv run --no-sync pytest
   ruff check src tests demos
   publish build

Usage
-----

.. code-block:: bash

   posamentier --help

Links
-----

- **Documentation**: https://geometor.github.io/posamentier
- **Repository**: https://github.com/geometor/posamentier
- **Issues**: https://github.com/geometor/posamentier/issues

License
-------

Licensed under the MIT License. See ``LICENSE`` for details.
