""" Order Handler

Supports [ GET, POST ]

"""

from . import common as c
import json

class Handler(c.BaseHandler):

    """Returns all orders given user_order ID.
    If ID is not provided, returns an error."""
    def get(self, id):
        if id is not None:
            query = """
                SELECT TO_CHAR(o_created_on, 'MM/DD/YYYY'),
                o_id, o_widget_id, o_configuration, o_user_order_id
                FROM {}.order WHERE o_user_order_id = {}
            """
            query = query.format(self.schema, id)
            cur = self.db.cursor()
            cur.execute(query)
            self.write(c.formatdata(cur))
        else:
            self.set_status(400)
            self.write('ERROR: ID must be specified in order to GET order.')

    """Create a new order. Orders expect data to be
    in the following format:
    {
      data: [{
          w_id: ID,
          p_ids: [ID]
      }]
    }
    """
    def post(self, *args):
        data = json.loads(self.get_arguments('data')[0].replace("'", '"'))

        # Create a new user order record
        query = """
            INSERT INTO {%1}.user_order (u_created_on)
            VALUES (DEFAULT)
            RETURNING u_id;
        """
        query = query.replace('{%1}', self.schema)
        cur = self.db.cursor()
        cur.execute(query)
        u_id = cur.fetchone()[0]

        # Create order records, linking each to user order
        for order in data:
            q2 = """
                INSERT INTO {%1}.order (o_widget_id, o_user_order_id, o_configuration)
                VALUES (%s, %s, %s)
                RETURNING o_id;
            """
            q2 = q2.replace('{%1}', self.schema)
            cur.execute(q2, (order['w_id'], u_id, list(map(int, order['p_ids']))))
            o_id = cur.fetchone()[0]

        self.db.commit()
        self.write(str(u_id))