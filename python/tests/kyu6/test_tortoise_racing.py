from codewars.kyu6.tortoise_racing import race


class TestTortoiseRacing():

    def test_tortoise_racing(self):
        assert race(720, 850, 70) == [0, 32, 18]
        assert race(80, 91, 37)   == [3, 21, 49]
        assert race(80, 100, 40)  == [2, 0, 0]
