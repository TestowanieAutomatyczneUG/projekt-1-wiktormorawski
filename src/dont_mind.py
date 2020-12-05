def Morse_coding(text):
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
    for letter in text:
        for trans_letter in translation:
            if letter.upper() == trans_letter[0]:
                result += trans_letter[1] + ' '
            else:
                pass
    return result
print(Morse_coding('śćżźąę€ółń'))