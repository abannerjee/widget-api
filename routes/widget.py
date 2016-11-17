"""Widget Route

Supports GET on specified widgets
"""

import tornado.web

class Handler(tornado.web.RequestHandler):
    def get(self, id):
        self.write("GET on Widget: {}".format(id))