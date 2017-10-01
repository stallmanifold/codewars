from itertools import accumulate


def regex_divisible_by(modulus):
    dfa = dfa_divisible_by(modulus)
    return dfa.to_regex()


def dfa_divisible_by(modulus):
    if modulus < 1:
        raise ValueError('Modulus too small. Use a modulus of at least 1.')
    
    alphabet = ['0', '1']
    starting_state = 0
    accepting_states = [0]
    next_state = dict((q, {}) for q in range(modulus))
    for q in next_state.keys():
        next_state[q]['0'] = (2*q + 0) % modulus
        next_state[q]['1'] = (2*q + 1) % modulus

    return Dfa(alphabet, next_state, starting_state, accepting_states)


class Dfa:

    def __init__(self, alphabet, next_state, starting_state, accepting_states):
        self.alphabet = alphabet
        self.next_state = next_state
        self.starting_state = starting_state
        self.accepting_states = accepting_states

    def eval(self, string):
        if not string:
            return False

        q = self.starting_state
        for ch in string:
            if ch in self.alphabet:
                q = self.next_state[q][ch]
            else:
                return False

        return q in self.accepting_states

    def to_regex(self):
        return NotImplemented

    def __str__(self):
        string =  'ALPHABET: {}\n'.format(self.alphabet)
        string += 'STARTING STATE: {}\n'.format(self.starting_state)
        string += 'ACCEPTING STATES: {}\n'.format('{}', self.accepting_states)
        string += 'STATE TABLE: \n'
        for q in self.next_state.keys():
            for bit in self.next_state[q].keys():
                string += 'next_state({}, \'{}\') == {}\n'\
                          .format(q, bit, self.next_state[q][bit])

        return string


def needs_parens(string):
    """
    Determine whether ``string`` is enclosed by parentheses. If it is not 
    enclosed by parentheses, it must be wrapped in them.
    """
    """
    if (len(string) > 1) and (string[0] == '(') and (string[-1] == ')'):
        return False
    else:
        return True
    """
    return not all(list(accumulate([0]+list(string), lambda curr,x: curr+1 if x == "(" else (curr-1 if x == ")" else curr)))[1:-1])


# TODO: sets too many parentheses, we only need them, if | is not already enclosed
def parenthesize(term):
    """
    Close ``term`` in parentheses if necessary.
    """
    if needs_parens(term) and '|' in term:
        return '(' + term + ')'
    
    return term


class RegexEq:

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def mult(eqn, factor):
        new_rhs = {}
        for term in eqn.rhs:
            new_rhs[term] = parenthesize(factor) + parenthesize(eqn.rhs[term])

        return RegexEq(eqn.lhs, new_rhs)

    def add(eqn1, eqn2):
        new_rhs = {}
        new_dict = eqn1.rhs.copy()
        new_dict.update(eqn2.rhs)
        for term in new_dict:
            new_rhs_term = '|'.join([x for x in [eqn1.rhs.get(term), eqn2.rhs.get(term)] if x != None])
            new_rhs[term] = new_rhs_term

        return RegexEq(eqn1.lhs, new_rhs)

    def reduce(self):
        """
        Apply Arden's rule to simplify a regular expression equation.
        """
        if self.lhs in self.rhs:
            r = self.rhs[self.lhs]
            self.rhs = RegexEq.mult(self, ('({})*' if needs_parens(r) else '{}*').format(r)).rhs
            self.rhs.pop(self.lhs, None)
        
        return self

    def substitute(eqn1, eqn2):
        new_rhs = dict((k, v) for k, v in eqn2.rhs.items() if k != eqn1.lhs)
        new_eqn = RegexEq(eqn2.lhs, new_rhs)

        return RegexEq.add(new_eqn, RegexEq.mult(eqn1, eqn2.rhs[eqn1.lhs]))

    def __str__(self):
        return 'Q[{}] = {}'.format(
            self.lhs, 
            ' + '.join('{} Q[{}]'.format(self.rhs[term], term) for term in self.rhs)
        )


class RegexSolver:
    
    def __init__(self, start, eqns):
        self.start = start
        self.eqns = eqns

    def __str__(self):
        return '\n'.join(str(eqn) for eqn in self.eqns.values())

    def solve_queue(self):
        queue = [self.eqns[self.start].lhs]
        for eqn in queue:
            for var in self.eqns[eqn].rhs:
                if (var not in queue) and (var != ''):
                    queue.append(var)

        queue.reverse()
        return queue

    def reduce_all(self):
        """ 
        Reduce every equation in ``self`` by applying Adren's rule.
        """
        for eqn in self.eqns.values():
            eqn.reduce()

    def solve(self):
        queue = self.solve_queue()
        for var in queue[:]:
            self.reduce_all()
            for lhs in queue:
                if var in self.eqns[lhs].rhs:
                    self.eqns[lhs] = self.eqns[var].substitute(self.eqns[lhs])
            
            queue.remove(var)

        return self.eqns[self.start].rhs['']


def make_solver(rem, modulus, base=2):
    equations = {}
    for state in range(modulus):
        state_dict = {}
        for inpt in range(base):
            key = (state*base + inpt) % modulus
            if key not in state_dict:
                state_dict[key] = str(inpt)
            else:
                state_dict[key] += ('|' + str(inpt))
        
        if state == rem:
            state_dict[''] = ''
        
        equations[state] = RegexEq(state, state_dict)

    return RegexSolver(0, equations)
