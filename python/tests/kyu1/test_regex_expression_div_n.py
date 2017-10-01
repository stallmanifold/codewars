import codewars.kyu1.regular_expression_div_n as r_mod_n
import re


class DfaDivN:

    def test_dfa_divisible_by_n(self):
        for modulus in range(20):
            dfa = r_mod_n.dfa_divisible_by(modulus)
            for n in range(1000):
                expected = n % modulus == 0
                result = dfa.eval(n)

                assert expected == result


class TestRegexExpressionDivN:

    def test_regex_expression_div_n(self):
        for modulus in range(1, 10):
            regex = r_mod_n.make_solver(0, modulus).solve()
            matcher = re.compile(regex)
            for n in range(1000):
                expected = bin(n)[2:]
                matched = matcher.fullmatch(expected)
                if n % modulus == 0:
                    assert matched
                else:
                    assert not matched
