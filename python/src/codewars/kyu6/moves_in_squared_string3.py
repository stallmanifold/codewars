def rot_90_clock(string):
    return '\n'.join(''.join(line) for line in zip(*string.split('\n')[::-1]))

def diag_1_sym(string):
    stride = len(string.split('\n')[0])
    if stride == 0:
        return ''

    return '\n'.join(string[i:len(string):stride+1] for i in range(stride))

def selfie_and_diag1(string):
    return '\n'.join('|'.join(line) for line in zip(string.split('\n'), diag_1_sym(string).split('\n')))

def oper(fct, string):
    return fct(string)
