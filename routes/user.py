""" Users Handler

Supports [ GET, POST ]

"""

from . import common as c

class Handler(c.BaseHandler):
    def get(self, id):
        self.write("GET on user: {}".format(id))

    def post(self):
        self.write("POST on user")