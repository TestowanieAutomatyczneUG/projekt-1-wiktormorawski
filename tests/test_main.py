from main import Main
import unittest


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
        expected = Exception
        self.assertRaises(expected, self.temp.Morse_coding('śćżźąę€ółń'))
    def tearDown(self):
        self.test_object = None



if __name__ == '__main__':
    unittest.main()