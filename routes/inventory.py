""" Inventory Handler

Supports [ GET, POST ]

"""

from . import common as c
import json

class Handler(c.BaseHandler):

    """Returns the inventory given a WIDGET ID."""
    def get(self, id):
        if id is not None:
            query = "SELECT * FROM {}.inventory WHERE i_widget_id = {};".format(self.schema, id)
        else:
            query = "SELECT * FROM {}.inventory;".format(self.schema)

        cur = self.db.cursor()
        cur.execute(query)
        self.write(c.formatdata(cur))

    """Updates inventory. Orders expect data to be
    in the following format:
    {
        w_id: ID,
        stock: NUM
    }
    """
    def post(self, *args):
        print(self.get_arguments('w_id'))
        print(self.get_arguments('stock'))
        w_id = json.loads(self.get_arguments('w_id')[0])
        stock = json.loads(self.get_arguments('stock')[0])

        # Updates inventory record
        query = """
            UPDATE {%1}.inventory
            SET i_stock = %s
            WHERE i_widget_id = %s
        """
        query = query.replace('{%1}', self.schema)
        cur = self.db.cursor()
        cur.execute(query, (stock, w_id))

        self.db.commit()
        self.write('Update on inventory')