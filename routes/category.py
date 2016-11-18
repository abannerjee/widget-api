""" Category Handler

Supports [ GET ]

GET - Returns all categories in the DB
      A category is defined as a property with
      'category' == 'type'
"""

from . import common as c

class Handler(c.BaseHandler):
    def get(self):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM widget.property WHERE category = 'type'")
        self.write(c.formatdata(cur))