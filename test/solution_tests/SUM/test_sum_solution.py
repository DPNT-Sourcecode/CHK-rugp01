from lib.solutions.SUM.sum_solution import SumSolution


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

    # def test_sum_out_of_range(self):
    #     assert SumSolution().compute(-1, 101) == ValueError


