""" Widgets Handler

Supports [ GET ]

"""

from . import common as c
from pydash import py_
import urllib.parse as urllib
import json

class Handler(c.BaseHandler):

    """Returns all 'widgets' matching query parameters if provided
    otherwise just returns all widgets.
    If duplicate parameters are defined, only the first one is considered."""
    def get(self, *args):
        url = self.request.uri
        qs = urllib.urlsplit(url)
        parsed = urllib.parse_qs(qs.query)

        query = """
            WITH all_inherited_widgets AS (
                SELECT w_id, w_name, unnest(w_inherit) FROM {%1}.widget
            )
            SELECT w_id, w_name, p_id, p_category, p_name, p_value FROM {%1}.widget_property wp
            JOIN {%1}.widget w ON (wp.wp_widget_id = w.w_id)
            JOIN {%1}.property p ON (wp.wp_property_id = p.p_id)
            WHERE w.w_id = ANY (SELECT unnest FROM all_inherited_widgets);
        """
        query = query.replace('{%1}', self.schema)
        cur = self.db.cursor()
        cur.execute(query)

        """Check if the query parameters are valid."""
        data = c.parsedata(cur)
        categories = py_.pluck(data, 'p_category')
        valid_params = py_.intersection(parsed.keys(), categories)
        data_by_id = py_.group_by(data, 'w_id')

        """For each widget, create a new widget object to return."""
        widgets = []
        for wid in data_by_id.keys():
            this = data_by_id[wid]
            by_cat = py_.group_by(this, 'p_category')
            p_cats = py_.pluck(this, 'p_category')
            p_names = py_.pluck(this, 'p_name')

            widget = {
                'w_id': wid,
                'w_name': py_.uniq(py_.pluck(this, 'w_name'))[0],
                'properties': dict(zip(p_cats, p_names)),
                'match': False
            }

            """Check if each property associated with the
            widget matches the query parameters."""
            for key in valid_params:
                if key in by_cat.keys():
                    widget['match'] = py_.contains(py_.pluck(by_cat[key], 'p_name'), parsed[key][0])

            widgets.append(widget)

        # If query parameters are not provided, return all widgets
        if len(valid_params) == 0:
            ret = widgets
        else:
            ret = py_.filter(widgets, {'match': True})

        self.write(json.dumps(ret, indent=4, separators=(',', ': ')))