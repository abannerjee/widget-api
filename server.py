#!/usr/bin/env python

"""Main API Server

Provides the REST API for the Widget Factory app.
"""

from tornado.ioloop import IOLoop
from routes import *
import tornado.web
import logging
import sys
import pgdb

config = {
    'app_port': 3000,
    'db_port': 5432,
    'host': '127.0.0.1',
    'db': 'widgetdb',
    'user': 'widgetapi',
    'schema': 'widget',
    'logformat': '%(asctime)s %(levelname)s: %(message)s',
    'logfile': 'server.log',
    'loglevel': logging.DEBUG
}

class Application(tornado.web.Application):
    def __init__(self, cfg=config):
        try:
            self.db = pgdb.connect(cfg)
            self.schema = cfg['schema']
        except:
            logging.error('Unable to connect to the database')
            sys.exit(1)

        routes = [
            (r"/user/([0-9]+)|/user", user.Handler),
            (r"/widget/([0-9]+)", widget.Handler),
            (r"/widgets/?|(\?|\&)([^=]+)\=([^&]+)", widgets.Handler),
            (r"/categories", category.Handler),
            (r"/sub_categories/?|(\?|\&)([^=]+)\=([^&]+)", subcategory.Handler),
            (r"/widget_categories", widgetcategory.Handler),
            (r"/order/([0-9]+)|/order", order.Handler)
        ]

        super(Application, self).__init__(routes)

def setupLogging():
    logging.basicConfig(
        format=config['logformat'],
        filename=config['logfile'],
        level=config['loglevel']
    )
    logging.info('Starting server on {}:{}'.format(config['host'], config['app_port']))

def main():
    setupLogging()
    app = Application()
    app.listen(config['app_port'])
    IOLoop.current().start()

if __name__ == "__main__":
    main()