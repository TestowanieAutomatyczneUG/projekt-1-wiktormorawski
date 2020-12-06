from src.main import Main
import unittest
from nose.tools import assert_equal, assert_raises
from parameterized import parameterized, parameterized_class


class TestAffine(unittest.TestCase):
    def setUp(self):
        self.temp = Main()

    @parameterized.expand([
        ('VENI', 3, 12, 'XYZK'),
        ('cAbM', 3, 12, 'sMpW'),
        ('iueghish', 7, 8, 'mskyfmef'),
        ('kolokwium', 19, 16, 'ywrwysmgk')
    ])
    def test_Affine_coding_equal_string(self, text, a, b, expected):
        self.assertEqual(self.temp.Affine_coding(text, a, b), expected)

    @parameterized.expand([
        ('VENI VICI', 9, 123, 'ADGN ANLN'),
        ('Na Statek Kamraci', 15, 12, 'Zm Wlmlug Gmkhmqc'),
        ('DO wozu BRACIE', 15, 8, 'BK aktw XDIMYQ'),
        ('kolokwium jest za dwa dni', 21, 6, 'iodoiasky nmup lg rag rts')
    ])
    def test_Affine_coding_equal_string_with_space(self, text, a, b, expected):
        self.assertEqual(self.temp.Affine_coding(text, a, b), expected)

    @parameterized.expand([
        ('dawdawdwadaw', 9, 123),
        ('NNNNa St KOMANDORE', 15, 12),
        ('AKODWANI', 15, 8),
        ('kol', 21, 6),
        ('    ', 19, 16)
    ])
    def test_Affine_coding_equal_string_lengths(self, text, a, b):
        self.assertEqual(len(self.temp.Affine_coding(text, a, b)), len(text))
