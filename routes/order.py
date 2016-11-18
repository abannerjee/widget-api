""" Order Handler

Supports [ GET, POST, PUT, DELETE ]

"""

from . import common as c

class Handler(c.BaseHandler):
    def get(self, id):
        self.write("GET on order")

    def post(self):
        self.write("POST on order")

    def put(self):
        self.write("PUT on order")

    def delete(self):
        self.write("DELETE on order")