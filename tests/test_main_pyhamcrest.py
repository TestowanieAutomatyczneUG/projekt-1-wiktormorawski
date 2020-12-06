import unittest
from hamcrest import *
from main import Main


class TestCeasar(unittest.TestCase):
    def setUp(self):
        self.temp = Main()

    def test_Instance_temp_Main(self):
        assert_that(self.temp, is_(Main))
    """Ceasar coding"""
    def test_ceasar_coding_equal_values_1(self):
        assert_that(self.temp.Ceasar_coding('abc'), equal_to('def'))

    def test_ceasar_coding_equal_values_2(self):
        assert_that(self.temp.Ceasar_coding('def'), equal_to('ghi'))

    def test_ceasar_coding_equal_last_indexed_letters(self):
        assert_that(self.temp.Ceasar_coding('XYZ'), equal_to('ABC'))

    def test_ceasar_coding_letter_lower_and_at_the_end_of_indexes(self):
        assert_that(self.temp.Ceasar_coding('avwxyz'), equal_to('dyzabc'))

    def test_ceasar_coding_number_as_parameter_raises_valueerror(self):
        assert_that(calling(self.temp.Ceasar_coding).with_args(1234), raises(ValueError))

    def test_ceasar_coding_number_string_as_parameter_raises_valueerror(self):
        assert_that(calling(self.temp.Ceasar_coding).with_args('123444'), raises(ValueError))

    def test_ceasar_coding_not_letters_as_parameter_raises_valueerror(self):
        assert_that(calling(self.temp.Ceasar_coding).with_args('@#$%^^^'), raises(ValueError))

    """Ceasar decoding"""
    def test_ceasar_decoding_equal_values_1(self):
        assert_that(self.temp.Ceasar_decoding('XYZ'), equal_to('UVW'))
    def tearDown(self):
        self.temp = Main()
