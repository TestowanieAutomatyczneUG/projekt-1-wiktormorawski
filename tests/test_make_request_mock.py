import requests
import unittest
from src.main import Main
from unittest.mock import patch


class TestHTTPIErequest(unittest.TestCase):
    def setUp(self):
        self.temp = Main()

    def test_not_received(self):
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value.status_code.return_value = 200
            assert self.temp.Make_request() == "Bye Bye"
