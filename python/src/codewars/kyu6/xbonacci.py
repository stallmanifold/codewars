import functools


def xbonacci(signature, n):
    if n < 0: 
        return []
    if n <= len(signature): 
        return signature[:n]

    return functools.reduce(
        lambda l, _: l + [sum([l[i] for i in range(len(l)-1, len(l) - len(signature)-1,-1)])], range(n-len(signature)), signature)
