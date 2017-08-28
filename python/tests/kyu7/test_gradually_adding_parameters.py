from codewars.kyu7.gradually_adding_parameters import add


class TestGraduallyAddingParameters():

    def test_gradually_adding_parameters(self):
        assert add() == 0
        assert add(100,200,300) == 1400
        assert add(2) == 2
