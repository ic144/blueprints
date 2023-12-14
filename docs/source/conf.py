"""Blueprints docs configuration."""
from blueprints import __version__
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath("../../"))

# project information
project = "Blueprints"
author = "Blueprints"
copyright = f"{datetime.now().year}, Blueprints v{__version__}"

# sphinx config
templates_path = ["_templates"]
exclude_patterns = ["_build"]

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "matplotlib.sphinxext.plot_directive",
    "nbsphinx",
    "sphinx_click",
    "sphinx_copybutton",
    "sphinxext.opengraph",
]

# autodoc config
autodoc_member_order = "bysource"
autodoc_typehints = "both"
autodoc_typehints_description_target = "documented_params"

# napoleon config
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_ivar = True

# nbsphinx config
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc=figure.dpi=96",
]

# intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "shapely": ("https://shapely.readthedocs.io/en/stable/", None),
}

# html theme
html_theme = "furo"
# html_logo = "_static/placeholder-logo.png"
html_static_path = ["_static"]
html_favicon = "_static/light_favicon.ico"
html_theme_options = {
    "light_logo": "placeholder-logo-light.png",  # add light mode logo
    "dark_logo": "placeholder-logo-dark.png",  # add dark mode logo
    "sidebar_hide_name": True,  # hide name of project in sidebar (already in logo)
    "source_repository": "https://github.com/Blueprints-org/blueprints",
    "source_branch": "main",
    "source_directory": "docs/",
}
pygments_style = "sphinx"
pygments_dark_style = "monokai"
