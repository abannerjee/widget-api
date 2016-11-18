from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application
from tornado.httpserver import HTTPRequest
import server
import unittest

class TestWidgetHandler(AsyncHTTPTestCase):

    def get_app(self):
        return server.Application()

    def test_widget_get(self):
        response = self.fetch('/widget/2')
        self.assertEqual(response.code, 200)

if __name__ == '__main__':
    unittest.main()