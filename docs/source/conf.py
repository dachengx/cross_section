# Configuration file for the Sphinx documentation builder.

# -- Project information

import xsectron

project = "Xsectron"
copyright = "2023, Dacheng Xu"

release = xsectron.__version__
version = xsectron.__version__

# -- General configuration

extensions = [
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for NAPOLEON output

napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output

epub_show_urls = "footnote"

# -- Options for TODO output

todo_include_todos = True


def setup(app):
    # Hack to import something from this dir. Apparently we're in a weird
    # situation where you get a __name__  is not in globals KeyError
    # if you just try to do a relative import...
    import os
    import sys

    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    from build_release_notes import convert_release_notes

    convert_release_notes()
