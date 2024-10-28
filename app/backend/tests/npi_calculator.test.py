from app.utils.npi_calculator import NpiCalculator

import unittest

class NpiCalculatorTest(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.npi = NpiCalculator()

    def test_valid_expression(self):
        expr = "5 1 2 + 4 * + 3 -"
        result = self.npi.evaluate(expr)

        self.assertEqual(result, 14)

    def test_invalid_expression(self):
        expr = "5 1 2 + 4 * + 3 -"
        result = self.npi.evaluate(expr)

        self.assertNotEqual(result, 15)

    def test_error_expression(self):
        expr = "5 1 2 + 4 * + 3 -"
        result = self.npi.evaluate(expr)

        self.assertRaises(ValueError, result)
