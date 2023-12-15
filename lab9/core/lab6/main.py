import sys
import unittest
import logging

sys.path.insert(0, '../lab2')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from tests import TestCalculator, TestSum, TestSubtraction, TestMultiplication, TestDivision


def main():
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.makeSuite(TestCalculator))
    test_suite.addTest(unittest.makeSuite(TestSum))
    test_suite.addTest(unittest.makeSuite(TestSubtraction))
    test_suite.addTest(unittest.makeSuite(TestMultiplication))
    test_suite.addTest(unittest.makeSuite(TestDivision))

    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)

    logger.info(f"Total tests run: {result.testsRun}")
    logger.info(f"Failures: {len(result.failures)}")
    logger.info(f"Errors: {len(result.errors)}")


if __name__ == '__main__':
    main()