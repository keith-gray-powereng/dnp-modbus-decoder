from django.test import TestCase
from django.test.client import Client


class TestIntegration(object):
    'Run the integration tests'
    def setUp(self):
        self.client = Client()

    def test_reset_remote_link(self):
        'Verifies a Reset Remote Link Message entered in the text area'
        response = client.get('/DNP3/DNP3/')
        print(response.status_code)
