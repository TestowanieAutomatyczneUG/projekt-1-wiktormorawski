import requests
import unittest
from src.main import Main
from unittest.mock import patch


class TestHTTPIErequest(unittest.TestCase):
    def setUp(self):
        self.temp = Main()

    def test_received(self):
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value.status_code = 200
            get_mock.return_value.text = "Allu"
            assert self.temp.Make_request() == "Allu" and type(self.temp.Make_request()) == str
    def test_not_received(self):
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value.status_code.return_value = 404
            assert self.temp.Make_request() == "Goodbye"

