def digits_base(base, x):
    digits = []
    num = x
    while num != 0:
        remainder = num % base
        num -= remainder
        num = num // base
        digits.append(remainder)

    digits.reverse()
    
    return digits


def digits_base10(x):
    return digits_base(10, x)


def from_digits(base, digits):
    num = 0
    base_sq = 1 
    for digit in digits:
        num     += base_sq * digit
        base_sq *= base

    return num

def from_digits_base10(digits):
    return from_digits(10, digits)

def descending_order(x):
    return from_digits_base10(sorted(digits_base10(x)))

def Descending_Order(x):
    """
    Compliance with problem definition.
    """
    return descending_order(x)
