""" Widget Handler

Supports [ GET, POST, PUT ]

"""

from . import common as c

class Handler(c.BaseHandler):
    def get(self, id):
        self.write("GET on widget: {}".format(id))

    def post(self):
        self.write("POST on widget")

    def put(self):
        self.write("PUT on widget")