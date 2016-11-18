#!/usr/bin/env python

"""Main API Server

Provides the REST API for the Widget Factory app.
"""
from tornado.ioloop import IOLoop
import tornado.web
import psycopg2
import logging


class Application(tornado.web.Application):
    def __init__(self):
        # PostgreSQL DB Connection shared across all handlers
        try:
            conn = psycopg2.connect("dbname='widgetdb' user='widgetapi' host='localhost'")
            self.db = conn
        except:
            logging.error('Error: Unable to connect to the database')

        urls = [
            (r"/widget/([0-9]+)", WidgetHandler),
        ]

        super(Application, self).__init__(urls)


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

class WidgetHandler(BaseHandler):
    def get(self, id):
        self.write("GET on widget: {}".format(id))


def main():
    app = Application()
    app.listen(3000)
    IOLoop.current().start()

if __name__ == "__main__":
    main()