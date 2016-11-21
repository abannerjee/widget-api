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

    def test_get_1(self):
        response = self.fetch('/subcategories?widget=1')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)
        self.assertEqual(len(res), 3)

    def test_get_2(self):
        response = self.fetch('/subcategories?widget=2')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)
        self.assertEqual(len(res), 5)

    def test_get_noparent(self):
        response = self.fetch('/subcategories')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)
        self.assertEqual(len(res), 5)

if __name__ == '__main__':
    unittest.main()