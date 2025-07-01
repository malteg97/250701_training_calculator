from testproject_calculator import calculator


class TestCalculator:

    def test_add(self):
        assert 4 == calculator.add(1, 3)
