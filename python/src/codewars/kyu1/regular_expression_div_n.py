def regex_divisible_by(modulus):
    dfa = Dfa.make(modulus)
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

    def to_regex(self):
        """
        Generate a regular expression from a DFA using the Brzozowski algerbaic method.
        """
        def trans(qi, ch, qj):
            if (qi in self.next_state) and (ch in self.next_state[qi]):
                if self.next_state[qi][ch] == qj:
                    return True
                else:
                    return False
            else:
                return False
        
        def star(term):
            if term == '':
                return ''
            else:
                return '(' + term + ')' + '*'

        # Initialize the terms that will appear in the regex.
        final_terms = dict((q, '') for q in self.next_state.keys())

        # Initialize the intermediate regex terms.
        terms = dict((q, {}) for q in self.next_state.keys())
        for qi in terms.keys():
            for qj in terms.keys():
                terms[qi][qj] = ''

        for qi in terms.keys():
            for qj in terms.keys():
                for ch in self.alphabet:
                    if trans(qi, ch, qj):
                        terms[qi][qj] = ch

        # Solve the equations to build the regex.
        for n in reversed(range(len(self.next_state))):
            final_terms[n] = star(terms[n][n]) + final_terms[n]
            for j in range(n):
                terms[n][j] = star(terms[n][n]) + terms[n][j]
            for i in range(n):
                final_terms[i] += '|' + '(' + terms[i][n] + final_terms[n] + ')'
                for j in range(n):
                    terms[i][j] += '|' + terms[i][n] + terms[n][j]

        return final_terms[0]

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
