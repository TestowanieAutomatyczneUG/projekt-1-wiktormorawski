class Main:
    def Morse_coding(self, text):
        translation = [(' ', '     '), ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'),
                       ('F', '..-.'),
                       ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
                       ('M', '--'), ('N', '-.'),
                       ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'), ('U', '..-'),
                       ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'), ('Z', '--..'), ('0', '-----'),
                       ('1', '.----'),
                       ('2', '..---'), ('3', '...--'), ('4', '....-'), ('5', '.....'), ('6', '-....'), ('7', '--...'),
                       ('8', '---..'), ('9', '----.')]
        result = ''
        polish_letters = ['ś','ć','ż','ź','ą','ę','€','ó','ł','ń']
        does_contain_polish_letters = False
        for letter in text:
            if letter not in polish_letters:
                for trans_letter in translation:
                    if letter.upper() == trans_letter[0]:
                        result += trans_letter[1] + ' '
            else:
                raise Exception('Contains polish letters')
        return result
