from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application
from tornado.httpserver import HTTPRequest
from test.config import config
import server
import unittest
import json
import urllib.parse

class TestOrderHandler(AsyncHTTPTestCase):

    def get_app(self):
        return server.Application(config)

    def test_widget_get(self):
        response = self.fetch('/widget/1')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)

    def test_order_post(self):
        data = {
          'data': [{
            'w_id': '1',
            'p_ids': ['1','5']
          }]
        }
        body = urllib.parse.urlencode(data)
        response = self.fetch('/order', method="POST", headers=None, body=body)
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)

if __name__ == '__main__':
    unittest.main()