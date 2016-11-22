""" Order Handler

Supports [ GET, POST, PUT, DELETE ]

"""

from . import common as c
import json

class Handler(c.BaseHandler):
    def get(self, id):
        self.write("GET on order")

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
        data = json.loads(self.get_arguments('data')[0])

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

    def put(self):
        self.write("PUT on order")

    def delete(self):
        self.write("DELETE on order")