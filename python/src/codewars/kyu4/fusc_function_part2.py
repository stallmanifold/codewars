def fusc2(n):
    a = 1
    b = 0
    while n > 0:
        if n % 2 == 1:
            b += a
            n = (n - 1) // 2
        else:
            a += b
            n = n // 2

    return b


def fusc(n):
    a = 1
    b = 0
    while n > 0:
        if n & 1:
            b += a
            n = (n - 1) // 2
        else:
            a += b
            n = n // 2

    return b
