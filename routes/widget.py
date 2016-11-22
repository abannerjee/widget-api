""" Widget Handler

Supports [ GET, POST ]

"""

from . import common as c
import json

class Handler(c.BaseHandler):

    """Returns a single widget with a matching ID"""
    def get(self, id):
        if id is not None:
            query = "SELECT * FROM {}.widget WHERE w_id = {}".format(self.schema, id)
            cur = self.db.cursor()
            cur.execute(query)
            self.write(c.formatdata(cur))
        else:
            self.set_status(400)
            self.write('ERROR: ID must be specified in order to GET widget.')

    """Create a new widget.
    Expect data to be in the following format:
    {
      data: {
          name: STR,
          type: ID,
          props: [ID]
      }
    }
    """
    def post(self, *arg):
        data = json.loads(self.get_arguments('data')[0].replace("'", '"'))

        # Create a new widget record
        query = """
            INSERT INTO {%1}.widget (w_name)
            VALUES (%s)
            RETURNING w_id;
        """
        query = query.replace('{%1}', self.schema)
        cur = self.db.cursor()
        cur.execute(query, (data['name'],))
        w_id = cur.fetchone()[0]

        # Create widget property records
        data['props'].append(data['type'])
        for p_id in data['props']:
            q2 = """
                INSERT INTO {%1}.widget_property (wp_widget_id, wp_property_id)
                VALUES (%s, %s)
                RETURNING wp_id;
            """
            q2 = q2.replace('{%1}', self.schema)
            cur.execute(q2, (w_id, p_id))
            o_id = cur.fetchone()[0]

        self.db.commit()
        self.write(str(w_id))