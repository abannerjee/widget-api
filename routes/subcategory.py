""" Sub-Category Handler

Supports [ GET ]

"""

from . import common as c

class Handler(c.BaseHandler):
    def get(self):
        self.write("GET on sub_categories")