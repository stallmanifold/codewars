from codewars.kyu4.valid_braces import validBraces


class TestValidBraces():

    def test_valid_braces(self):
        assert validBraces('()')     == True
        assert validBraces('[(])')   == False
        assert validBraces('(){}[]') == True
        assert validBraces('(}')     == False
        assert validBraces('[(])')   == False
        assert validBraces('([{}])') == True

