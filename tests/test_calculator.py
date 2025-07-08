from testproject_calculator import calculator


class TestCalculator:

    def test_add(self):
        assert 4 == calculator.add(1, 3)

    def test_multiply(self):
        assert 3 == calculator.multiply(1, 3)   

    def test_subtract(self):
        assert 2 == calculator.subtract(5, 3)           

    def test_divide(self):
        assert 2 == calculator.divide(6, 3)
        assert None is calculator.divide(6, 0)  

    def test_power(self):
        assert 8 == calculator.power(2, 3)
        assert 1 == calculator.power(2, 0)
        assert 0.25 == calculator.power(2, -2)
