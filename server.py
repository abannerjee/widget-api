#!/usr/bin/env python

"""Main API Server

Provides the REST API for the Widget Factory app.
"""
from tornado.ioloop import IOLoop
import tornado.web
import psycopg2
import logging
import sys
import json
import pgdb

log = {
    'format': '%(asctime)s %(levelname)s: %(message)s',
    'filename': 'server.log',
    'level': logging.DEBUG
}

options = {
    'app_port': 3000,
    'db_port': 5432,
    'host': '127.0.0.1',
    'db': 'widgetdb',
    'user': 'widgetapi'
}

class Application(tornado.web.Application):
    def __init__(self):
        try:
            self.db = pgdb.connect(options)
        except:
            logging.error('Error: Unable to connect to the database')
            sys.exit(1)

        urls = [
            (r"/user/([0-9]+)|/user", UserHandler),
            (r"/widget/([0-9]+)", WidgetHandler),
            (r"/widgets/?|(\?|\&)([^=]+)\=([^&]+)", WidgetsHandler),
            (r"/categories", CategoriesHandler),
            (r"/sub_categories/?|(\?|\&)([^=]+)\=([^&]+)", SubCategoriesHandler),
            (r"/widget_categories", WidgetCategoriesHandler),
            (r"/order/([0-9]+)|/order", OrderHandler)
        ]

        super(Application, self).__init__(urls)


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

class UserHandler(BaseHandler):
    def get(self, id):
        self.write("GET on user: {}".format(id))

    def post(self):
        self.write("POST on user")

class WidgetHandler(BaseHandler):
    def get(self, id):
        self.write("GET on widget: {}".format(id))

    def post(self):
        self.write("POST on widget")

    def put(self):
        self.write("PUT on widget")

class WidgetsHandler(BaseHandler):
    def get(self, delim, prop, val):
        self.write("GET on widgets")

# A Cateogry is defined as Property with a 'category' == 'type'.
# Returns all categories.
class CategoriesHandler(BaseHandler):
    def get(self):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM widget.property WHERE category = 'type'")
        self.write(formatdata(cur))

class SubCategoriesHandler(BaseHandler):
    def get(self):
        self.write("GET on sub_categories")

class WidgetCategoriesHandler(BaseHandler):
    def post(self):
        self.write("POST on widget categories")

    def delete(self):
        self.write("DELETE on widget categories")

class OrderHandler(BaseHandler):
    def get(self, id):
        self.write("GET on order")

    def post(self):
        self.write("POST on order")

    def put(self):
        self.write("PUT on order")

    def delete(self):
        self.write("DELETE on order")


# Transforms the rows returned after performing
# a DB query into a JSON object.
def formatdata(cur):
    labels = [x[0] for x in cur.description]
    rows = cur.fetchall()
    data = [dict(zip(labels, x)) for x in rows]
    return json.dumps(data, indent=4, separators=(',', ': '))

def setupLogging():
    logging.basicConfig(format=log['format'], filename=log['filename'], level=log['level'])
    logging.info('Server started on {}:{}'.format(options['host'], options['app_port']))

def main():
    setupLogging()
    app = Application()
    app.listen(options['app_port'])
    IOLoop.current().start()

if __name__ == "__main__":
    main()