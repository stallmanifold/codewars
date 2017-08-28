import functools


def tribonacci(signature, n):
    if n < 0: 
        return []

    return functools.reduce(
        lambda l, _: l + [l[len(l)-3] + l[len(l)-2] + l[len(l)-1]], range(n-3), signature[:n])
