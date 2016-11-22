""" Widget Handler

Supports [ GET, POST, PUT ]

"""

from . import common as c

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

    def post(self, *arg):
        #print(self.get_arguments('data'))
        self.write("POST on Widget")

    def put(self):
        self.write("PUT on Widget")