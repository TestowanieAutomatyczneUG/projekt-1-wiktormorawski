class Main:
    def Morse_coding(self, text):
        translation = [(' ', '   '), ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'),
                       ('F', '..-.'),
                       ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
                       ('M', '--'), ('N', '-.'),
                       ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'), ('U', '..-'),
                       ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'), ('Z', '--..'), ('0', '-----'),
                       ('1', '.----'),
                       ('2', '..---'), ('3', '...--'), ('4', '....-'), ('5', '.....'), ('6', '-....'), ('7', '--...'),
                       ('8', '---..'), ('9', '----.')]
        result = ''
        polish_letters = ['ś', 'ć', 'ż', 'ź', 'ą', 'ę', '€', 'ó', 'ł', 'ń']
        does_contain_polish_letters = False
        for letter in text:
            if letter not in polish_letters:
                for trans_letter in translation:
                    if letter.upper() == trans_letter[0]:
                        result += trans_letter[1] + ' '
            else:
                raise Exception('Contains polish letters')
        return result

    def Morse_decoding(self, morse_code):
        translation = [(' ', '   '), ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'),
                       ('F', '..-.'),
                       ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
                       ('M', '--'), ('N', '-.'),
                       ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'), ('U', '..-'),
                       ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'), ('Z', '--..'), ('0', '-----'),
                       ('1', '.----'),
                       ('2', '..---'), ('3', '...--'), ('4', '....-'), ('5', '.....'), ('6', '-....'), ('7', '--...'),
                       ('8', '---..'), ('9', '----.')]
        result = ''
        space_count = 0
        prepared_morse_code = morse_code.split(' ')

        def checkspacing(code):
            if code.count('') % 4 == 0:
                return True
            else:
                return False

        if not checkspacing(prepared_morse_code):
            raise Exception('Spacing between code words should be 5')
        for code in prepared_morse_code:
            if code == '':
                space_count += 1
                if space_count == 4:
                    result += ' '
                    space_count = 0
            for trans_letter_code in translation:
                if code == trans_letter_code[1]:
                    result += trans_letter_code[0]
        return result.lower()
