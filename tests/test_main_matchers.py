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


def check_result_contain_single_spaces_beetween_morse(self, previous_val):
    if " " not in previous_val:
        if self.val.count(" ") == len(previous_val):
            return self.val
        else:
            raise Exception('spaces does not match')
    else:
        raise Exception('Result does not contain spaces')


add_extension(check_result_contain_single_spaces_beetween_morse)
add_extension(check_result_length_higher_and_string_and_contain_spaces)


class Main_morse_coding_Matchers(unittest.TestCase):
    def setUp(self):
        self.temp = Main()

    def test_Morse_coding_check_result_length_higher_and_string_and_contain_spaces(self):
        argument = 'wiktor 1'
        assert_that(self.temp.Morse_coding(argument)).check_result_length_higher_and_string_and_contain_spaces(argument)

    def test_Morse_coding_check_result_contain_single_spaces_beetween_morse(self):
        argument = 'Testowanie'
        assert_that(self.temp.Morse_coding(argument)).check_result_contain_single_spaces_beetween_morse(argument)


def check_result_same_length__string__and__letters_same_case(self, previous_val):
    if len(self.val) == len(previous_val):
        if type(self.val) == str and type(previous_val) == str:
            if sum(1 for i in self.val if i.isupper()) == sum(1 for i in previous_val if i.isupper()):
                return self.val
            else:
                raise Exception('Not Same case')
        else:
            raise Exception('Invalid type of argument or result of operation')
    else:
        raise Exception('Not Same length')


add_extension(check_result_same_length__string__and__letters_same_case)


class Main_ceasar_coding_Matchers(unittest.TestCase):
    def setUp(self):
        self.temp = Main()

    def test_Ceasar_coding_check_result_same_length__string__and__letters_same_case(self):
        argument = 'wiKtOOOr'
        assert_that(self.temp.Ceasar_coding(argument)).check_result_same_length__string__and__letters_same_case(
            argument)

    def test_Ceasar_coding_check_result_same_length__string__and__letters_same_case_but_with_space(self):
        argument = 'wKK OKA'
        assert_that(self.temp.Ceasar_coding(argument)).check_result_same_length__string__and__letters_same_case(
            argument)


class Main_ceasar_decoding_Matchers(unittest.TestCase):
    def setUp(self):
        self.temp = Main()

    def test_Ceasar_decoding_check_result_same_length__string__and__letters_same_case_but_with_space(self):
        argument = 'MMMii doah'
        assert_that(self.temp.Ceasar_coding(argument)).check_result_same_length__string__and__letters_same_case(
            argument)

    def test_Ceasar_decoding_check_result_same_length__string__and__letters_same_case(self):
        argument = 'ConnORmCgregor'
        assert_that(self.temp.Ceasar_coding(argument)).check_result_same_length__string__and__letters_same_case(
            argument)


if __name__ == '__main__':
    unittest.main()
