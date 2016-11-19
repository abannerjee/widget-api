"""Category Handler

Supports [ GET ]

"""

from . import common as c

class Handler(c.BaseHandler):

    """ Returns all categories in the DB. A category is defined
    as a property with 'category' == 'type'."""
    def get(self):
        query = "SELECT * FROM {}.property WHERE p_category = 'type'".format(self.schema)
        cur = self.db.cursor()
        cur.execute(query)
        self.write(c.formatdata(cur))