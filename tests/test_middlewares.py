import os
import unittest
from typing import Dict

import django
from django.core.handlers.wsgi import WSGIRequest
from django_extensions import middlewares

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()


class GetClientIpTests(unittest.TestCase):

    def test_simple(self):
        params: Dict[str, str] = {
            'REQUEST_METHOD': 'GET',
            'wsgi.input': '',
            'REMOTE_ADDR': '127.0.0.0'
        }
        request = WSGIRequest(params)
        ip = middlewares._get_client_ip(request)

        self.assertEqual(ip, params['REMOTE_ADDR'])
