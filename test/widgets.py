from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application
from tornado.httpserver import HTTPRequest
from test.config import config
import server
import unittest
import json

class TestWidgetsHandler(AsyncHTTPTestCase):

    def get_app(self):
        return server.Application(config)

    def test_get(self):
        response = self.fetch('/widgets')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)
        self.assertEqual(len(res), 2)

    def test_get_valid_params(self):
        response = self.fetch('/widgets?color=test-color-1')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)
        self.assertEqual(len(res), 1)

    def test_get_invalid_params(self):
        response = self.fetch('/widgets?notreal=4&alsonotreal=9')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)
        self.assertEqual(len(res), 2)

    def test_get_invalid_valid_mix(self):
        response = self.fetch('/widgets?notreal=4&color=test-color-3')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)
        self.assertEqual(len(res), 1)

    def test_get_malformed_query(self):
        response = self.fetch('/widgets?notreal=4&color=&type')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)
        self.assertEqual(len(res), 2)

if __name__ == '__main__':
    unittest.main()