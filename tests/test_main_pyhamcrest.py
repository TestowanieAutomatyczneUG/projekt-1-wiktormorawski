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

    def test_ceasar_decoding_equal_values_2_going_back(self):
        assert_that(self.temp.Ceasar_decoding('ABC'), equal_to('XYZ'))

    def test_ceasar_decoding_letters_lower(self):
        assert_that(self.temp.Ceasar_decoding('wik'), equal_to('tfh'))

    def test_ceasar_decoding_letters_lower_and_start_indexes(self):
        assert_that(self.temp.Ceasar_decoding('ahj'), equal_to('xeg'))

    def test_ceasar_decoding_number_as_parameter_raises_valueerror(self):
        assert_that(calling(self.temp.Ceasar_decoding).with_args(997), raises(ValueError))

    def test_ceasar_decoding_number_string_as_parameter_raises_valueerror(self):
        assert_that(calling(self.temp.Ceasar_decoding).with_args('2000'), raises(ValueError))

    def test_ceasar_decoding_not_letters_as_parameter_raises_valueerror(self):
        assert_that(calling(self.temp.Ceasar_decoding).with_args('@#$%^^^'), raises(ValueError))

    def test_ceasar_decoding_lower_letters_with_space_start_indexes(self):
        assert_that(self.temp.Ceasar_decoding('abc def'), equal_to('xyz abc'))

    def test_ceasar_decoding_upper_letters_with_space_start_indexes(self):
        assert_that(self.temp.Ceasar_decoding('ABC DEF'), equal_to('XYZ ABC'))

    def test_ceasar_decoding_lower_upper_letters_with_space(self):
        assert_that(self.temp.Ceasar_decoding('xyz AC'), equal_to('uvw XZ'))

    def test_ceasar_decoding_blank_string(self):
        assert_that(len(self.temp.Ceasar_decoding('')), less_than(1))

    def tearDown(self):
        self.temp = Main()
