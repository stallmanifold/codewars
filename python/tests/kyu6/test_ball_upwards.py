from codewars.kyu6.ball_upwards import max_ball


class TestBallUpwards():

    def test_ball_upwards(self):
        assert max_ball(37) == 10
        assert max_ball(45) == 13
        assert max_ball(99) == 28
        assert max_ball(85) == 24
