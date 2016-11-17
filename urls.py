"""Urls and handlers

This file contains the endpoints currently
implemented by the API server and the
associated handlers.
"""

from routes import *

urls = [
    (r"/widget/([0-9]+)", widget.Handler)
]