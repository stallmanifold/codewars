def to_digits_base10(n):
    """
    Return the digits of a number in base 10.
    """
    digits = []
    remaining = n
    while remaining > 0:
        digit = remaining % 10
        remaining = (remaining - digit) // 10
        digits.append(digit)

    return digits[::-1]

def from_digits_base10(digits):
    """
    Convert a set of digits into a number in base 10.
    """
    result = 0
    for k in range(len(digits)):
        result = 10 * result + digits[k]

    return result

def swap(digits, i, j):
    digits[i], digits[j] = digits[j], digits[i]

def next_bigger(n):
    """
    Calculate the smallest number larger than ``n`` whose digits are
    a permutation of the digits of ``n``.
    """
    digits = to_digits_base10(n)
    num_digits = len(digits)

    # Going from right to left, skip the digits already in 
    # ascending order.
    i = num_digits - 1 if num_digits > 0 else 0
    while i > 0:
        if digits[i] > digits[i - 1]:
            break

        i -= 1

    # If no digits change, ``n`` is the largest permutation 
    # of its digits.
    if i == 0:
        return -1
         
    digit = digits[i - 1]
    i_smallest = i
    for j in range(i + 1, num_digits):
        if digits[j] > digit and digits[j] < digits[i_smallest]:
            i_smallest = j

    swap(digits, i_smallest, i - 1)
    digits = digits[:i] + sorted(digits[i:])
      
    return from_digits_base10(digits)
