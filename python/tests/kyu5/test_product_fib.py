from codewars.kyu5.product_fib import productFib


class TestProductFib():

    def test_product_fib(self):
        assert productFib(4895) == [55, 89, True]
        assert productFib(5895) == [89, 144, False]
