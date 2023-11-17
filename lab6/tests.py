import sys
import unittest
import logging
# Add the parent directory to the sys.path if not already present
sys.path.insert(0, '../lab2')

# Now you can import your Calculator and other classes
from operations.calculator import Calculator, Sum, Subtraction, Multiplication, Division, Power, SquareRoot


# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestCalculator(unittest.TestCase):

    def test_valid_input(self):
        logger.info("Running test_valid_input")
        calculator = Calculator("+", 2, 3)
        self.assertEqual(calculator.operation, "+")
        self.assertEqual(calculator.first_number, 2)
        self.assertEqual(calculator.second_number, 3)

    def test_invalid_operator(self):
        logger.info("Running test_invalid_operator")
        with self.assertRaises(ValueError):
            calculator = Calculator("&", 2, 3)

    def test_invalid_first_number(self):
        logger.info("Running test_invalid_first_number")
        with self.assertRaises(ValueError):
            calculator = Calculator("+", "abc", 3)

# Similar modifications for other test classes...

class TestSum(unittest.TestCase):

    def test_sum_positive_numbers(self):
        logger.info("Running test_sum_positive_numbers")
        calculator = Sum(2, 3)
        result = calculator.calculate()
        logger.info(f"Result: {result}")
        self.assertEqual(result, 5)

    def test_sum_negative_numbers(self):
        logger.info("Running test_sum_negative_numbers")
        calculator = Sum(-2, -3)
        result = calculator.calculate()
        logger.info(f"Result: {result}")
        self.assertEqual(result, -5)

    def test_sum_mixed_numbers(self):
        logger.info("Running test_sum_mixed_numbers")
        calculator = Sum(2, -3)
        result = calculator.calculate()
        logger.info(f"Result: {result}")
        self.assertEqual(result, -1)

class TestSubtraction(unittest.TestCase):

    def test_subtract_positive_numbers(self):
        logger.info("Running test_subtract_positive_numbers")
        calculator = Subtraction(5, 3)
        result = calculator.calculate()
        logger.info(f"Result: {result}")
        self.assertEqual(result, 2)

    def test_subtract_negative_numbers(self):
        logger.info("Running test_subtract_negative_numbers")
        calculator = Subtraction(-5, -3)
        result = calculator.calculate()
        logger.info(f"Result: {result}")
        self.assertEqual(result, -2)

    def test_subtract_mixed_numbers(self):
        logger.info("Running test_subtract_mixed_numbers")
        calculator = Subtraction(2, -3)
        result = calculator.calculate()
        logger.info(f"Result: {result}")
        self.assertEqual(result, 5)


class TestMultiplication(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        logger.info("Running test_multiply_positive_numbers")
        calculator = Multiplication(2, 3)
        result = calculator.calculate()
        logger.info(f"Result: {result}")
        self.assertEqual(result, 6)

    def test_multiply_negative_numbers(self):
        logger.info("Running test_multiply_negative_numbers")
        calculator = Multiplication(-2, -3)
        result = calculator.calculate()
        logger.info(f"Result: {result}")
        self.assertEqual(result, 6)

    def test_multiply_mixed_numbers(self):
        logger.info("Running test_multiply_mixed_numbers")
        calculator = Multiplication(2, -3)
        result = calculator.calculate()
        logger.info(f"Result: {result}")
        self.assertEqual(result, -6)

class TestDivision(unittest.TestCase):

    def test_divide_positive_numbers(self):
        logger.info("Running test_divide_positive_numbers")
        calculator = Division(6, 3)
        result = calculator.calculate()
        logger.info(f"Result: {result}")
        self.assertEqual(result, 2)

    def test_divide_negative_numbers(self):
        logger.info("Running test_divide_negative_numbers")
        calculator = Division(-6, -3)
        result = calculator.calculate()
        logger.info(f"Result: {result}")
        self.assertEqual(result, 2)

    def test_divide_mixed_numbers(self):
        logger.info("Running test_divide_mixed_numbers")
        calculator = Division(8, -4)
        result = calculator.calculate()
        logger.info(f"Result: {result}")
        self.assertEqual(result, -2)

    def test_divide_by_zero(self):
        logger.info("Running test_divide_by_zero")
        calculator = Division(5, 0)
        result = calculator.calculate()
        logger.info(f"Result: {result}")
        self.assertIsNone(result)
