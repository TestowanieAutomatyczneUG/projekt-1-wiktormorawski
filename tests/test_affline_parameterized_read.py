import unittest
from src.main import Main


class TestAffinRead(unittest.TestCase):
    def setUp(self):
        self.temp = Main()

    def test_Affin_decoding_equal_string(self):
        file = open("../data/tests_parameterized")
        for line in file:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                pass
            else:
                data = line.split(" ")
                code, a, b, expected = data[0], int(data[1].strip("\n")), int(data[2].strip("\n")), data[3].strip("\n")
                self.assertEqual(self.temp.Affine_decoding(code, a, b), expected)
        file.close()

    def test_Affin_decoding_equal_string_with_space(self):
        file = open("../data/tests_parameterized_with_spaces")
        for line in file:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                pass
            else:
                data = line.split(" ")
                code, a, b, expected = data[0] + " " + data[1], int(data[2].strip("\n")), int(data[3].strip("\n")), data[4].strip("\n") + " " + data[5].strip("\n")
                self.assertEqual(self.temp.Affine_decoding(code, a, b), expected)
        file.close()

    def tearDown(self):
        self.temp = None


if __name__ == "__main__":
    unittest.main()
