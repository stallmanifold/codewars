import codewars.kyu8.multiply as mult


class TestMultiply():

    def test_multiply1(self):
        a = 3
        b = 4
        assert mult.multiply(a, b) == a * b

    def test_multiply2(self):
        a = -34
        b = 99
        assert mult.multiply(a, b) == a * b
        assert mult.multiply(a, b) < 0
