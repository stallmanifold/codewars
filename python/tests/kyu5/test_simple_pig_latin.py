from codewars.kyu5.simple_pig_latin import pig_it


class TestSimplePigLatin():

    def test_pig_latin1(self):
        string   = 'Pig latin is cool'
        expected = 'igPay atinlay siay oolcay'
        actual = pig_it(string)

        assert actual == expected

    def test_pig_latin2(self):
        string = 'This is my string'
        expected = 'hisTay siay ymay tringsay'
        actual = pig_it(string)

        assert actual == expected

    def test_pig_latin_should_be_same_on_empty_input(self):
        assert pig_it('') == ''
        assert pig_it('     ') == '     '
