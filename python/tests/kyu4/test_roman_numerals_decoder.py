from codewars.kyu4.roman_numerals_decoder import solution


class TestRomanNumeralsDecoder():

    def test_roman_numerals_decoder(self):
        assert solution('XXI') == 21
        assert solution('MCMXC') == 1990
        assert solution('MMVIII') == 2008
        assert solution('I') == 1
        assert solution('II') == 2
        assert solution('III') == 3
        assert solution('IV') == 4
        assert solution('V') == 5
        assert solution('VI') == 6
        assert solution('VII') == 7
        assert solution('VIII') == 8
        assert solution('IX') == 9
        assert solution('X') == 10
        assert solution('XI') == 11
        assert solution('XXX') == 30
        assert solution('MDCLXVI') == 1666
