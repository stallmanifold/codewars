import re


MORSE_CODE = {
    '.-':     'A', '-...':    'B', '-.-.':   'C', '-..':       'D', '.':       'E', '..-.': 'F',
    '--.':    'G', '....':    'H', '..':     'I', '.---':      'J', '-.-':     'K', '.-..': 'L',
    '--':     'M', '-.':      'N', '---':    'O', '.--.':      'P', '--.-':    'Q', '.-.':  'R',
    '...':    'S', '-':       'T', '..-':    'U', '...-':      'V', '.--':     'W', '-..-': 'X',
    '-.--':   'Y', '--..':    'Z',
    '-----':  '0', '.----':   '1', '..---':  '2', '...--':     '3',  '....-':  '4',
    '.....':  '5', '-....':   '6', '--...':  '7', '---..':     '8',  '----.':  '9',
    '.-.-.-': '.', '--..--':  ',', '..--..': '?', '.----.':    '\'', '-.-.--': '!',
    '-..-.':  '/', '-.--.':   '(', '-.--.-': ')', '.-...':     '&',  '---...': ':',
    '-.-.-.': ';', '-...-':   '=', '.-.-.':  '+', '-....-':    '-',  '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}

UN_MORSE_CODE = dict(((v, k) for (k, v) in MORSE_CODE.items()))


def encode_morse(message):
    message = message.strip()
    morse = ''
    char_count = len(message)
    i = 0
    while i < char_count:
        if (message[i] == 'S') and ((i + 2) < char_count):
            if message[i:i + 3] == 'SOS':
                morse += UN_MORSE_CODE[message[i:i + 3]]
                i += 3
            elif message[i + 1] != ' ':
                morse += UN_MORSE_CODE[message[i]] + ' '
                i += 1
            else:
                morse += UN_MORSE_CODE[message[i]] + '   '
                i += 2
        elif (message[i] != ' '):
            if (i + 1 < char_count) and (message[i + 1] != ' '):
                morse += UN_MORSE_CODE[message[i]] + ' '
                i += 1
            elif (i + 1 < char_count) and (message[i + 1] == ' '):
                morse += UN_MORSE_CODE[message[i]] + '   '
                i += 2
            else:
                morse += UN_MORSE_CODE[message[i]]
                i += 1
        else:
            morse += '   '
            i += 1

    return morse


def encode_bits(morse_code, period=1):
    PERIOD = { '.' : 1, '-' : 3 }
    
    char_count = len(morse_code)
    bits = ''
    i = 0
    while i < char_count:
        if (i + 1 < char_count) and (morse_code[i] != ' ') and (morse_code[i + 1] == ' '):
            # We are either at the end of a character, or we are at the end of a word.
            spaces_found = 0
            j = i + 1
            while (j < char_count) and (morse_code[j] == ' '):
                spaces_found += 1
                j += 1

            bits += '1' * PERIOD[morse_code[i]] * period

            if spaces_found < 3:
                # We are between characters. We use a convention that excess spaces 
                # less than 3 are interpreted as a single space.
                bits += '000' * period
            else:
                # We are between words.
                bits += '0000000' * period

            i += spaces_found
        elif (i + 1 < char_count) and (morse_code[i] != ' ') and (morse_code[i + 1] != ' '):
            # We are inside a character.
            bits += '1' * PERIOD[morse_code[i]] * period + '0' * period
            i += 1
        elif (i + 1 == char_count) and (morse_code[i] != ' '):
            # We are at the end of the message.
            bits += '1' * PERIOD[morse_code[i]] * period
            i += 1
        else:
            # The spaces are padding at either beginning or the end 
            # of the message.
            i += 1

    return bits


def decode_morse(morse_code):
    words = morse_code.strip().split('   ')
    return ' '.join(''.join(MORSE_CODE[c] for c in w.split(' ') if c is not '') for w in words)


def decode_bits(bits):
    bits = bits.strip('0')
    seqs = [len(s) for s in re.findall('(1+|0+)', bits)]
    period = min(seqs) if seqs is not [] else 1
    morse = bits.replace('0000000'*period, '   ')\
                .replace('000'*period, ' ')\
                .replace('111'*period, '-')\
                .replace('1'*period, '.')\
                .replace('0'*period, '')
    return morse