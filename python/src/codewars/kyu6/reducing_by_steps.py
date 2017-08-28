def gcdi(a, b):
    def go(a, b):
        if b == 0:
            return a
        else:
            return gcdi(b, a % b)

    return go(abs(a), abs(b))
        
def lcmu(a, b):
    return abs(a * b) / gcdi(a, b)
    
def som(a, b):
    return a + b
    
def maxi(a, b):
    if a > b: return a
    else: return b
    
def mini(a, b):
    if a < b: return a
    else: return b
    
def oper_array(fct, arr, init): 
    if len(arr) == 0:
        return []

    output = [fct(init, arr[0])]
    for i in range(1, len(arr)):
        output.append(fct(output[i-1], arr[i]))

    return output

