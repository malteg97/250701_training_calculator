from testproject_calculator import calculator


class TestCalculator:

    def test_add(self):
        assert 4 == calculator.add(1, 3)
    
    def test_multiply(self):
        assert 6 == calculator.multiply(2, 3)

    def test_subtract(self):
        assert 1 == calculator.subtract(3, 2)

    def test_divide(self):
        assert 2 == calculator.divide(6, 3)
        assert None is calculator.divide(6, 0)


