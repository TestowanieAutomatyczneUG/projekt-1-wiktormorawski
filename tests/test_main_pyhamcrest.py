import unittest
from hamcrest import *
from main import Main


class TestCeasar(unittest.TestCase):
    def setUp(self):
        self.temp = Main()

    def test_Instance_temp_Main(self):
        assert_that(self.temp, is_(Main))

    def test_ceasar_coding_equal_values1(self):
        assert_that(self.temp.Ceasar_coding('abc'), equal_to('def'))
