from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application
from tornado.httpserver import HTTPRequest
from test.config import config
import server
import unittest
import json
import urllib.parse

class TestWidgetHandler(AsyncHTTPTestCase):

    def get_app(self):
        return server.Application(config)

    def test_widget_get(self):
        response = self.fetch('/widget/1')
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]['w_name'], 'test-widget')

    def test_widget_get_noid(self):
        response = self.fetch('/widget')
        self.assertEqual(response.code, 400)

    """
    def test_widget_post(self):
        data = {'data': {'type': 'test-type'}}
        body = urllib.parse.urlencode(data)
        response = self.fetch('/widget', method="POST", headers=None, body=body)
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)

    def test_widget_put(self):
        data = {'data': {'type': 'test-type'}}
        body = urllib.parse.urlencode(data)
        response = self.fetch('/widget', method="POST", headers=None, body=body)
        res = json.loads(response.body.decode('utf-8'))
        self.assertEqual(response.code, 200)
    """


if __name__ == '__main__':
    unittest.main()