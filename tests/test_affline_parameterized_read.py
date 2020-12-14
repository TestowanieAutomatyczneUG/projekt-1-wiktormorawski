import unittest

from nose.tools import assert_equal, assert_raises

from src.main import Main


class TestAffinRead(unittest.TestCase):
    def setUp(self):
        self.temp = Main()

    def test_Affin_decoding_equal_string(self):
        file = open("data/tests_parameterized")
        for line in file:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                pass
            else:
                data = line.split(" ")
                code, a, b, expected = data[0], int(data[1].strip("\n")), int(data[2].strip("\n")), data[3].strip("\n")
                self.assertEqual(self.temp.Affine_decoding(code, a, b), expected)
        file.close()

    def test_Affin_decoding_equal_string_with_space(self):
        file = open("data/tests_parameterized_with_spaces")
        for line in file:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                pass
            else:
                data = line.split(" ")
                code, a, b, expected = data[0] + " " + data[1], int(data[2].strip("\n")), int(data[3].strip("\n")), data[4].strip("\n") + " " + data[5].strip("\n")
                self.assertEqual(self.temp.Affine_decoding(code, a, b), expected)
        file.close()

    def test_Affin_decoding_first_parameter_wrong(self):
        file = open("data/tests_parameterized_exceptions")
        for line in file:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                pass
            else:
                data = line.split(" ")
                code, a, b = data[0], int(data[1].strip("\n")), int(data[2].strip("\n"))
                assert_raises(ValueError, self.temp.Affine_decoding, code, a, b)
        file.close()

    def test_Affin_decoding_second_or_third_parameter_wrong(self):
        file = open("data/tests_parameterized_exceptions_second_or_third")
        for line in file:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                pass
            else:
                data = line.split(" ")
                code, a, b = data[0], int(data[1].strip("\n")), int(data[2].strip("\n"))
                assert_raises(ValueError, self.temp.Affine_decoding, code, a, b)
        file.close()

    def test_Affin_decoding_float_raise_error(self):
        file = open("data/tests_parameterized_exceptions_second_or_third_float")
        for line in file:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                pass
            else:
                data = line.split(" ")
                code, a, b = data[0], float(data[1].strip("\n")), float(data[2].strip("\n"))
                assert_raises(ValueError, self.temp.Affine_decoding, code, a, b)
        file.close()

    def tearDown(self):
        self.temp = None


if __name__ == "__main__":
    unittest.main()
