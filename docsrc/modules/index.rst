:order: 90

=======
Modules
=======

API summary for ``geometor.posamentier``:

- :mod:`geometor.posamentier` — Public package interface exporting ``__version__`` and :func:`~geometor.posamentier.app.run`.
- :mod:`geometor.posamentier.app` — Command-line parser (:func:`~geometor.posamentier.app.build_parser`) and entry point (:func:`~geometor.posamentier.app.main`).
- :mod:`geometor.posamentier.catalog` — Typed catalog manifest descriptor (:class:`~geometor.posamentier.catalog.CatalogEntrySpec`), loader (:func:`~geometor.posamentier.catalog.load_catalog_manifest`), and exact-algebra guard (:func:`~geometor.posamentier.catalog.assert_no_floats`).
