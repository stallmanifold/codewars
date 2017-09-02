def fusc(n):
    assert type(n) == int and n >= 0
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    elif (n % 2 == 0): 
        return fusc(n // 2)
    else:
        return fusc((n - 1)//2) + fusc((n - 1)//2 + 1)
