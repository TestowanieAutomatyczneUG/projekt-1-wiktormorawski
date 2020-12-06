from src.main import Main
import unittest
from nose.tools import assert_equal, assert_raises
from parameterized import parameterized, parameterized_class


class TestAffine(unittest.TestCase):
    def setUp(self):
        self.temp = Main()

    @parameterized.expand([
        ('VENI', 3, 12, 'XYZK')
    ])
    def test_Affine_coding_equal_string(self, text, a, b, expected):
        self.assertEqual(self.temp.Affine_coding(text, a, b), expected)
