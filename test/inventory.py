from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application
from tornado.httpserver import HTTPRequest
from test.config import config
import server
import unittest
import json
import urllib.parse

class TestInventoryHandler(AsyncHTTPTestCase):

    def get_app(self):
        return server.Application(config)

    def test_inventory_get(self):
        response = self.fetch('/inventory/1')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)
        self.assertEqual(len(res), 1)

    def test_inventory_post(self):
        data = { 'w_id': '2', 'stock': '11' }
        body = urllib.parse.urlencode(data)
        response = self.fetch('/inventory', method="POST", headers=None, body=body)
        res = response.body.decode('utf-8')
        self.assertEqual(response.code, 200)

if __name__ == '__main__':
    unittest.main()