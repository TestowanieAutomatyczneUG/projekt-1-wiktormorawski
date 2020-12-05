from main import Main
import unittest
from assertpy import assert_that
'only unittest and assertpy'

class TestMain(unittest.TestCase):
    def setUp(self):
        self.temp = Main()
    def test_morse_coding_value_equal_wiktor(self):
        expected = '.-- .. -.- - --- .-. '
        self.assertEqual(expected, self.temp.Morse_coding('wiktor'))
    def test_morse_coding_value_equal_ryba(self):
        expected = '.-. -.-- -... .- '
        self.assertEqual(expected, self.temp.Morse_coding('ryba'))
    def test_morse_coding_polish_letters(self):
        assert_that(self.temp.Morse_coding).raises(Exception).when_called_with('śćżźąę€ółń')
    def test_morse_coding_with_sentence(self):
        assert_that(self.temp.Morse_coding('Ala ma kota')).is_equal_to('.- .-.. .-     -- .-     -.- --- - .- ')
    def test_morse_decoding_to_text_without_space_between_equal(self):
        expected = 'mrozonka'
        assert_that(self.temp.Morse_decoding('-- .-. --- --.. --- -. -.- .- ')).is_equal_to(expected)
    def tearDown(self):
        self.test_object = None



if __name__ == '__main__':
    unittest.main()