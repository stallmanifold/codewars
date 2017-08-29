from codewars.kyu4.twice_linear import dbl_linear


class TestTwiceLinear():
    
    def test_twice_linear(self):  
        assert dbl_linear(10) == 22
        assert dbl_linear(20) == 57
        assert dbl_linear(30) == 91
        assert dbl_linear(50) == 175
