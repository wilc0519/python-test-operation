import unittest
from factorial import factorial_number

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        number = 3
        fact = factorial_number(number)
        self.assertEqual(fact, 6)

    def test_factorial(self):
        number = 1
        fact = factorial_number(number)
        self.assertEqual(fact, 1)    

