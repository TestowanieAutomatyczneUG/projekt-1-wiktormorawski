
import unittest
from src.main import Main
class TestAffinRead(unittest.TestCase):
    def test_Affin_decoding_equal_string(self):
        self.temp = Main()
        file = open("../data/tests_parameterized")
        for line in file:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                pass
            else:
                data = line.split(" ")
                code, a, b, expected = data[0], int(data[1].strip("\n")), int(data[2].strip("\n")), data[3].strip("\n")
                self.assertEqual(self.temp.Affine_decoding(code, a, b), expected)
        file.close()
    

if __name__ == "__main__":
    unittest.main()