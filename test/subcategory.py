from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application
from tornado.httpserver import HTTPRequest
from test.config import config
import server
import unittest
import json

class TestSubCategoryHandler(AsyncHTTPTestCase):

    def get_app(self):
        return server.Application(config)

    def test_get(self):
        response = self.fetch('/subcategories?parent=1')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)
        self.assertEqual(len(res), 1)

    def test_get_noparent(self):
        response = self.fetch('/subcategories')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)
        self.assertEqual(len(res), 1)

if __name__ == '__main__':
    unittest.main()