from collections import Callable


class BalanceMapper(Callable):
    """
    The class ```BalanceMapper``` decides the any language of balanced
    characters.
    """
    def __init__(self, left_charmap):
        self.left_charmap  = dict(left_charmap)
        self.right_charmap = dict((v,k) for k,v in left_charmap.items())

    def __call__(self, string):
        stack = []
        for char in string:
            if char in self.left_charmap:
                stack.append(char)
            elif char in self.right_charmap:
                try:
                    if stack.pop() != self.right_charmap[char]:
                        return False
                except:
                    return False
            else:
                return False

        # If the stack is empty when we've parsed the string,
        # the string is a valid string of balanced characters.
        if stack == []:
            return True
        else:
            return False


group_check = BalanceMapper({ '(': ')', '[': ']', '{': '}'})
