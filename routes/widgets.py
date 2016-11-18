""" Widgets Handler

Supports [ GET ]

"""

from . import common as c

class Handler(c.BaseHandler):
    def get(self, delim, prop, val):
        self.write("GET on widgets")