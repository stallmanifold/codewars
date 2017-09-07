from codewars.kyu4.decode_the_morse_code_part2 import encode_morse, decode_morse, encode_bits, decode_bits


class TestDecodeMorePart2():

    def cases(self):
        return [
            'HEY JUDE',
            'MORSE CODE',
            'MORE MORSE CODE!!',
            'KVqjrYR5tj2XbtoljzurKU5T9uqRU3N9w1marAq3AWWGMo9o7UsDG8dZrQiY',
            '8rFizqRjDSWhLpIsSC6byBfDhc30yh6eUDAfqh313IVEZW5h6It8urdT4EIC',
            '',
            '@',
            #'...--   ...---...   ....    ',
            'SOS',
            '   MORSE CODE!! SO MUCH MORSE CODE!!!    '
        ]

    def test_decode_and_encode_inverses(self):
        tests = self.cases()
        for test in tests:
            assert decode_morse(encode_morse(test.upper())) == test.upper().strip()
            morse = encode_morse(test.upper())
            assert encode_morse(decode_morse(morse)) == morse

    def test_decode_encode_should_correctly_parse_sos(self):
        assert encode_morse('SOS') == '...---...'
        assert encode_morse('  SOS   ') == '...---...'
        assert encode_morse('  SO S   ') != '...---...'

    def test_encode_bits_and_decode_bits_inverses(self):
        tests = self.cases()
        for test in tests:
            print(test)
            morse = encode_morse(test.upper())
            print(morse)
            for period in range(1, 4):
                assert decode_bits(encode_bits(morse, period)) == morse
