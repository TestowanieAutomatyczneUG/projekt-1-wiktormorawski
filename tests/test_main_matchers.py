import unittest
from assertpy import add_extension, assert_that, contains
from src.main import Main


def check_result_length_higher_and_string_and_contain_spaces(self, previous_val):
    if len(self.val) > len(previous_val):
        if type(self.val) == str:
            if " " in previous_val:
                if "   " in self.val:
                    return self.val
                else:
                    raise Exception(f'{self.val} doesnt contain space')
            else:
                raise Exception('argument doesnt contain space')
        else:
            raise Exception(f'{self.val} is not a string')
    else:
        raise Exception(f'{self.val} is not longer')

add_extension(check_result_length_higher_and_string_and_contain_spaces)

class Main_morse_coding_decoding_Matchers(unittest.TestCase):
    def setUp(self):
        self.temp = Main()

    def test_Morse_coding_check_result_length_higher_and_string_and_contain_spaces(self):
        argument = "wiktor 1"
        assert_that(self.temp.Morse_coding(argument)).check_result_length_higher_and_string_and_contain_spaces(argument)


if __name__ == '__main__':
    unittest.main()
