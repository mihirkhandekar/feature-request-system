import unittest
from unittest.mock import patch

import app


class ViewsTest(unittest.TestCase):

    def setUp(self):
        self.app = app.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.payload = None

    @unittest.skip("API not called")
    def test_add(self):  # Issue in calling API
        response = self.client.post('/api/featurerequest', json=self.payload)
        self.assertEqual(response.status_code, 201)

    @unittest.skip("API not called")
    def test_get(self):  # Issue in calling API
        response = self.client.get('/api/featurerequest')
        self.assertEqual(response.status_code, 200)
