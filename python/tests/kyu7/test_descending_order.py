from codewars.kyu7.descending_order import descending_order


class TestDescendingOrder():

    def test_descending_order(self):
        assert descending_order(0) == 0
        assert descending_order(15) == 51
        assert descending_order(123456789) == 987654321
        assert descending_order(12344437) == 74443321
