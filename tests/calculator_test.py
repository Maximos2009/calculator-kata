import unittest
from calculator import calculate
from utils import generate_int


class CalculatorTest(unittest.TestCase):
    def test_empty_string_should_return_zero(self):
        actual = calculate("")

        self.assertEqual(actual, 0)

    def test_single_number_return_that_number(self):
        number = generate_int()
        actual = calculate(str(number))

        self.assertEqual(actual, number)

    def test_two_add_operation(self):
        number1 = generate_int()
        number2 = generate_int()
        number3 = generate_int()
        expected = number1 + number2 + number3

        actual = calculate(f"{number1} + {number2} + {number3}")

        self.assertEqual(actual, expected)

    def test_add_then_minus_operation(self):
        number1 = generate_int()
        number2 = generate_int()
        number3 = generate_int()
        expected = number1 + number2 - number3
        value = f"{number1} + {number2} - {number3}"

        actual = calculate(value)

        self.assertEqual(actual, expected, f"{value} != {expected}")

    def test_plus_and_multiple_operation(self):
        number1 = generate_int()
        number2 = generate_int()
        number3 = generate_int()
        expected = number1 + number2 * number3
        value = f"{number1} + {number2} * {number3}"

        actual = calculate(value)

        self.assertEqual(actual, expected, f"{value} != {expected}")
