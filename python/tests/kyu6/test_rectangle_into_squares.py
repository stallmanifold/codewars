from codewars.kyu6.rectangle_into_squares import sq_in_rect


class TestRectangleIntoSquares():

    def test_big_square_should_fail(self):
        length = 5
        width  = 5
        actual = sq_in_rect(5, 5)
        expected = None

        assert actual == expected

    def test_square_tiling_of_rectangle(self):
        length = 5
        width  = 5
        actual = sq_in_rect(5, 3)
        expected = [3, 2, 1, 1]

        assert actual == expected

        actual = sq_in_rect(3, 5)
        expected = [3, 2, 1, 1]

        assert actual == expected
