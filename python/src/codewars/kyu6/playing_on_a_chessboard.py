from fractions import Fraction

def __game(n):
    total = sum(Fraction(m,m+k) for m in range(1,n+1) for k in range(1,n+1))
    if total.denominator != 1:
        return [total.numerator, total.denominator]
    else:
        return [total.numerator]

def game1(n):
    if n % 2 == 0:
        return [(n + n*(n-1)) // 2]
    else:
        return [n + n*(n-1), 2]

# The code golf version
game = lambda n: {0: [n*n // 2], 1: [n*n, 2]}[n % 2]
