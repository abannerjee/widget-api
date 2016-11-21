""" Common classes and functions used
by the handlers
"""

import tornado.web
import json

class BaseHandler(tornado.web.RequestHandler):
    @property
    def schema(self):
        return self.application.schema

    @property
    def db(self):
        return self.application.db

def parsedata(cur):
    labels = [x[0] for x in cur.description]
    rows = cur.fetchall()
    data = [dict(zip(labels, x)) for x in rows]
    return data

def formatdata(cur):
    data = parsedata(cur)
    return json.dumps(data, indent=4, separators=(',', ': '))