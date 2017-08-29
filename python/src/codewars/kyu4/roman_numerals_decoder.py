import enum


class RomanNumeral(enum.Enum):
    NULL = 0  # Sentinel value.
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000


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
            if current.value >= after.value:
                total += current.value
            else:
                total -= current.value

        return total
    
    def from_string(string):
        for ch in string:
            if not RomanNumeral.__members__[ch] in RomanNumeral.__members__.values():
                return None

        return RomanNumber(string)

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

def solution(string):
    return RomanNumber.from_string(string).decimal
