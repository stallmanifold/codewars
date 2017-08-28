def add(*args):
    return sum(i * v for i,v in enumerate(args, start=1))

# add = lambda *xs: sum(i*x for i,x in enumerate(xs, 1))