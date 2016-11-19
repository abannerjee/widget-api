""" Sub-Category Handler

Supports [ GET ]

"""

from . import common as c
import urllib.parse as urllib

class Handler(c.BaseHandler):

    """Returns all 'properties' matching a parent id if provided
    otherwise just returns all 'properties' where parent id is not null"""
    def get(self, *args):
        url = self.request.uri
        qs = urllib.urlsplit(url)
        parsed = urllib.parse_qs(qs.query)

        if 'parent' in parsed:
            query = "SELECT * FROM {}.property WHERE p_parent = {}".format(self.schema, parsed['parent'][0])
        else:
            query = "SELECT * FROM {}.property WHERE p_parent IS NOT NULL".format(self.schema)

        cur = self.db.cursor()
        cur.execute(query)
        self.write(c.formatdata(cur))