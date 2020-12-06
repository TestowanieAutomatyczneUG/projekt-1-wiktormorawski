class Main:
    def __init__(self):
        self.translation = [(' ', '   '), ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'),
                            ('F', '..-.'),
                            ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
                            ('M', '--'), ('N', '-.'),
                            ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
                            ('U', '..-'),
                            ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'), ('Z', '--..'), ('0', '-----'),
                            ('1', '.----'),
                            ('2', '..---'), ('3', '...--'), ('4', '....-'), ('5', '.....'), ('6', '-....'),
                            ('7', '--...'),
                            ('8', '---..'), ('9', '----.'), (',', '--..--'), ('.', '.-.-.-'), ('?', '..--..'),
                            (';', '-.-.-.'), (':', '---...'), ('/', '-..-.'), ('_', '..--.-'), ('!', '-.-.--'),
                            ('-', '-....-'), ('+', '.-.-.'), ('(', '-.--.'), (')', '-.--.-'), ('=', '-...-'),
                            ('@', '.--.-.')]

        self.correct_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                'R',
                                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8',
                                '9', ' ']

        self.correct_codes = ['', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-',
                              '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--',
                              '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....',
                              '--...', '---..', '----.', '--..--', '.-.-.-', '..--..', '-.-.-.', '---...', '-..-.',
                              '..--.-', '-.-.--', '-....-', '.-.-.', '-.--.', '-.--.-', '-...-', '.--.-.']

        self.ceasar_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                'I',
                                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def Morse_coding(self, text):
        result = ''
        for letter in text:
            if letter.upper() in self.correct_letters:
                for trans_letter in self.translation:
                    if letter.upper() == trans_letter[0]:
                        result += trans_letter[1] + ' '
            else:
                raise Exception('Contains incorrect letters')
        return result

    def Morse_decoding(self, morse_code):
        result = ''
        space_count = 0
        prepared_morse_code = morse_code.split(' ')

        def checkspacing(code):
            if code.count('') % 4 == 0:
                return True
            else:
                return False

        if not checkspacing(prepared_morse_code):
            raise Exception('Spacing between code words should be equal to 5')
        for code in prepared_morse_code:
            if code not in self.correct_codes:
                raise Exception('Incorrect code')
            if code == '':
                space_count += 1
                if space_count == 4:
                    result += ' '
                    space_count = 0
            for trans_letter_code in self.translation:
                if code == trans_letter_code[1]:
                    result += trans_letter_code[0]
        return result.lower()

    def Ceasar_coding(self, text):
        result = ''
        if type(text) != str:
            raise ValueError
        for letter in text:
            if letter not in self.ceasar_alphabet:
                if letter == " ":
                    result += " "
                else:
                    raise ValueError
            else:
                ceasar_index = self.ceasar_alphabet.index(letter) + 3
                if letter.isupper() and ceasar_index > 51:
                    ceasar_index -= 26
                if letter.islower() and ceasar_index > 25:
                    ceasar_index -= 26
                result += (self.ceasar_alphabet[ceasar_index])
        return result

    def Ceasar_decoding(self, code):
        result = ''
        if type(code) != str:
            raise ValueError
        for coded_letter in code:
            if coded_letter not in self.ceasar_alphabet:
                if coded_letter == " ":
                    result += " "
                else:
                    raise ValueError
            else:
                letter_index = self.ceasar_alphabet.index(coded_letter) - 3
                if coded_letter.isupper() and letter_index < 26:
                    letter_index += 26
                if coded_letter.islower() and letter_index < 0:
                    letter_index += 26
                result += (self.ceasar_alphabet[letter_index])
        return result

    def Affine_coding(self, text, a, b):
        result = ''
        for letter in text:
            if letter == " ":
                result += " "
            else:
                affine_index = ((self.ceasar_alphabet.index(letter) * a) + b) % 52
                if letter.isupper() and affine_index < 26:
                    affine_index += 26
                if letter.islower() and affine_index > 25:
                    affine_index -= 26
                result += (self.ceasar_alphabet[affine_index])
        return result
