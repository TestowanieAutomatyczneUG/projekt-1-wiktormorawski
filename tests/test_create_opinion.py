import requests
import unittest
from src.main import Main
from unittest.mock import patch


class TestCreateOpinion(unittest.TestCase):
    def setUp(self):
        self.temp = Main()

