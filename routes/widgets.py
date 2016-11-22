""" Widgets Handler

Supports [ GET ]

"""

from . import common as c
from pydash import py_
import urllib.parse as urllib
import json

class Handler(c.BaseHandler):

    """Returns all 'widgets' matching query parameters if provided
    otherwise just returns all widgets."""
    def get(self, *args):
        url = self.request.uri
        qs = urllib.urlsplit(url)
        parsed = urllib.parse_qs(qs.query)

        """Placeholder for supporting inheritance.
        Inheritance is currently not implemented."""
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

        """Create a hash with widget id as key."""
        data_by_id = py_.group_by(data, 'w_id')

        """For each widget, create a new widget object to return."""
        widgets = []
        for wid in data_by_id.keys():
            this = data_by_id[wid]
            by_cat = py_.group_by(this, 'p_category')
            uniq_cat = py_.uniq(py_.pluck(this, 'p_category'))

            widget = {
                'w_id': wid,
                'w_name': py_.uniq(py_.pluck(this, 'w_name'))[0],
                'match': True
            }

            """Create a new key, val pair for each property
            for the widget."""
            for cat in uniq_cat:
                widget[cat] = py_.pluck(by_cat[cat], 'p_name')

            """Check if each property associated with the
            widget matches the query parameters."""
            for key in valid_params:
                if key in by_cat.keys():
                    widget['match'] = widget['match'] and len(py_.intersection(widget[key], parsed[key])) > 0

            widgets.append(widget)

        """If query parameters are not provided or invalid,
        return all widgets without filtering."""
        if len(valid_params) == 0:
            ret = widgets
        else:
            ret = py_.filter(widgets, {'match': True})

        self.write(json.dumps(ret, indent=4, separators=(',', ': ')))