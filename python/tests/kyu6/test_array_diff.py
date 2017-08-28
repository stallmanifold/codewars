from codewars.kyu6.array_diff import array_diff


class TestArrayDiff():

    def test_array_diff(self):
        assert array_diff([1,2],   [1])   == [2]
        assert array_diff([1,2,2], [1])   == [2,2]
        assert array_diff([1,2,2], [2])   == [1]
        assert array_diff([1,2,2], [])    == [1,2,2]
        assert array_diff([],      [1,2]) == []
