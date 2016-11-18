#!/usr/bin/env python

"""Main API Server

Provides the REST API for the Widget Factory app.
"""
from tornado.ioloop import IOLoop
import tornado.web
import psycopg2
import logging

options = {
    'app_port': 3000,
    'db_port': 5432,
    'host': '127.0.0.1',
    'db': 'widgetdb',
    'user': 'widgetapi'
}

class Application(tornado.web.Application):
    def __init__(self):
        # PostgreSQL DB Connection shared across all handlers
        try:
            constr = "dbname='{}' user='{}' host='{}' port='{}'".format(
                options['db'],
                options['user'],
                options['host'],
                options['db_port']
            )
            conn = psycopg2.connect(constr)
            self.db = conn
        except:
            logging.error('Error: Unable to connect to the database')

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
    def get(self, delim, prop, val)
        self.write("GET on widgets")

class CategoriesHandler(BaseHandler):
    def get(self):
        self.write("GET on categories")

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


def main():
    app = Application()
    app.listen(options['app_port'])
    IOLoop.current().start()

if __name__ == "__main__":
    main()