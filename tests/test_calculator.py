from testproject_calculator import calculator


class TestCalculator:

    def test_add(self):
        assert 4 == calculator.add(1, 3), f"Addition fehlgeschlagen"

    def test_multiply(self):
        assert 15 == calculator.multiply(5, 3), f"Multiplikation fehlgeschlagen"

    def test_subtract(self):
        assert 2 == calculator.subtract(5, 3), f"Subtraktion fehlgeschlagen"

    def test_divide(self):
        assert 2 == calculator.divide(6, 3), f"Division fehlgeschlagen"
