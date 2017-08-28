from codewars.kyu6.xbonacci import xbonacci


class TestXbonacci():

    def test_xbonacci(self):
        assert xbonacci([0,1],10) == [0,1,1,2,3,5,8,13,21,34]
        assert xbonacci([1,1],10) == [1,1,2,3,5,8,13,21,34,55]
        assert xbonacci([0,0,0,0,1],10) == [0,0,0,0,1,1,2,4,8,16]
        assert xbonacci([1,0,0,0,0,0,1],10) == [1,0,0,0,0,0,1,2,3,6]
        assert xbonacci([1,0,0,0,0,0,0,0,0,0],20) == [1,0,0,0,0,0,0,0,0,0,1,1,2,4,8,16,32,64,128,256]
