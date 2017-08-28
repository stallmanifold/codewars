from functools import reduce as fold


def in_array(array1, array2):
    return sorted(
        fold(set.union, 
             map(set, map(lambda s2: filter(lambda s1: s1 in s2, array1), array2)), set()))
