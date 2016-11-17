"""Main API Server

Provides the REST API for the Widget Factory app.
"""
from tornado.ioloop import IOLoop
from tornado.web import Application
from urls import urls

def make_app():
    return Application(urls)

def main():
    app = make_app()
    app.listen(3000)
    IOLoop.current().start()

if __name__ == "__main__":
    main()