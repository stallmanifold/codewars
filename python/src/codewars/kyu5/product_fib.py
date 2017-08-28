def fibs(n):
    current, next = 0, 1
    for _ in range(n):
        yield (current, next)
        current, next = next, current + next


def productFib(prod):
    if prod < 0:
        return [0, 1, False]

    for m, n in fibs(prod):
        if m * n == prod:
            return [m, n, True]
        if m * n > prod:
            return [m, n, False]
