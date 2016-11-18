""" Widget-Category Handler

Supports [ POST, DELETE ]

"""

from . import common as c

class Handler(c.BaseHandler):
    def post(self):
        self.write("POST on widget categories")

    def delete(self):
        self.write("DELETE on widget categories")