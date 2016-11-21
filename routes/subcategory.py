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

        if 'widget' in parsed:
            query = """
                WITH all_inherited_widgets AS (
                    SELECT unnest(w_inherit) FROM {%1}.widget WHERE w_id = {%2}
                )
                SELECT p_id, p_category, p_name, p_value FROM {%1}.widget_property wp
                JOIN {%1}.widget w ON (wp.wp_widget_id = w.w_id)
                JOIN {%1}.property p ON (wp.wp_property_id = p.p_id)
                WHERE w.w_id = ANY (SELECT * FROM all_inherited_widgets)
                AND p.p_category != 'type';
            """
            query = query.replace('{%1}', self.schema).replace('{%2}', parsed['widget'][0])
        else:
            query = "SELECT * FROM {}.property WHERE p_category != 'type'".format(self.schema)

        cur = self.db.cursor()
        cur.execute(query)
        self.write(c.formatdata(cur))