import itertools

"""
def to_pig_latin(word):
    if word[0] is True:
        return word[1][1:] + word[1][0] + 'ay'
    else:
        return word[1]

def groupers(string):
    return itertools.groupby(string, lambda ch: ch.isalnum())

def chunks(string):
    return map(lambda p: (p[0], ''.join(p[1])), groupers(string))

def pig_it(text):
    return ''.join(map(to_pig_latin, chunks(text)))
"""

to_pig_latin = lambda w: { 
        w[0] is True : lambda w: w[1][1:] + w[1][:1] + 'ay', 
        w[0] is False: lambda w: w[1]
    }[True](w)

groupers = lambda st: itertools.groupby(st, lambda ch: ch.isalnum())
chunks   = lambda st: ((w[0], ''.join(w[1])) for w in groupers(st))

pig_it = lambda text: ''.join(map(to_pig_latin, chunks(text)))
