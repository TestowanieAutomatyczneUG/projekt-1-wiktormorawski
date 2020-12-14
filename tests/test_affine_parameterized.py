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


@parameterized_class(('text', 'a', 'b', 'expected'), [
    ("1234", 3, 2, ValueError),
    (1234, 2, 2, ValueError),
    ("ŚĄŚ", 4, 12, ValueError),
    ("!@#!$%#@", 11, 13, ValueError),
    (-12, 8, 18, ValueError),
    (0.2, 2, 2, ValueError)
])
class Affin_coding_first_parameter_wrong(unittest.TestCase):
    def setUp(self):
        self.temp = Main()

    def test_valueErrors(self):
        assert_raises(self.expected, self.temp.Affine_coding, self.text, self.a, self.b)

    def tearDown(self):
        self.temp = None


@parameterized_class(('text', 'a', 'b', 'expected'), [
    ("wiktor", -3, 2, TypeError),
    ("filip", 0.2, 2, TypeError),
    ("adam", '4', 12, TypeError),
    ("andrzej", 11, -13, TypeError),
    ("MARCIN", 8, 0.18, TypeError),
    ("JANEK", 2, "2", TypeError),
    ("Kuba", -22, -13, TypeError),
    ("JAKKuba", 0.22, 1.3, TypeError),
    ("aiufhsoie", '7', '12', TypeError)
])
class Affin_coding_second_or_third_parameter_wrong(unittest.TestCase):
    def test_valueErrors(self):
        temp = Main()
        assert_raises(self.expected, temp.Affine_coding, self.text, self.a, self.b)


@parameterized([("1234", 3, 2),
                (1234, 2, 2),
                ("ŚĄŚ", 4, 12),
                ("!@#!$%#@", 11, 13),
                (-12, 8, 18),
                (0.2, 2, 2)])
def test_Affin_decoding_first_parameter_wrong(code, a, b):
    temp = Main()
    assert_raises(ValueError, temp.Affine_decoding, code, a, b)
