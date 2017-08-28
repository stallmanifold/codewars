import codewars.kyu6.reducing_by_steps as problem


class TestReducingBySteps():

    def test_reducing_by_steps(self):
        def testing(actual, expected):
            assert actual == expected

        a = [ 18, 69, -90, -78, 65, 40 ]

        r = [ 18, 3, 3, 3, 1, 1 ]
        op = problem.oper_array(problem.gcdi, a, a[0])
        testing(op, r)
        r = [ 18, 414, 2070, 26910, 26910, 107640 ]
        op = problem.oper_array(problem.lcmu, a, a[0])
        testing(op, r)
        r = [ 18, 87, -3, -81, -16, 24 ]
        op = problem.oper_array(problem.som, a, 0)
        testing(op, r)
        r = [ 18, 18, -90, -90, -90, -90 ]
        op = problem.oper_array(problem.mini, a, a[0])
        testing(op, r)
        r = [ 18, 69, 69, 69, 69, 69 ]
        op = problem.oper_array(problem.maxi, a, a[0])
        testing(op, r)
