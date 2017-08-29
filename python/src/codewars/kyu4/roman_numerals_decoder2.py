class RomanNumeral():
    NULL = 0  # Sentinel value.
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

    __members__ = { 'I' : I, 'V' : V, 'X' : X, 'L' : L, 'C' : C, 'D' : D, 'M' : M }


class RomanNumber():
    __KEYS = dict((v,k) for (k,v) in RomanNumeral.__members__.items())

    def __init__(self, string):
        self.numerals = []
        for ch in string:
            self.numerals.append(RomanNumeral.__members__[ch])

        self.numerals.append(RomanNumeral.NULL)
        self.__total = self.__to_decimal()
    
    def __to_decimal(self):
        total = 0
        for (current, after) in zip(self.numerals[:-1], self.numerals[1:]):
            if current >= after:
                total += current
            else:
                total -= current

        return total

    def __str__(self):
        string = ''
        for numeral in self.numerals[:-1]:
            string += self.__KEYS[numeral]

        return string

    def __repr__(self):
        return 'RomanNumber({})'.format(str(self.numerals))

    @property
    def decimal(self):
        return self.__total


def from_string(string):
    for ch in string:
        if not RomanNumeral.__members__[ch] in RomanNumeral.__members__.values():
            return None

    return RomanNumber(string)


def solution(string):
    return from_string(string).decimal
