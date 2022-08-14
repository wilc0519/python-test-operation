import unittest
from factorial import factorial_number

class TestFactorial(unittest.TestCase):
    def test_factorial_numbers_greater_than_one(self):
        number = 3
        fact = factorial_number(number)
        self.assertEqual(fact, 6)

    def test_factorial_of_uno(self):
        number = 1
        fact = factorial_number(number)
        self.assertEqual(fact, 1)   

    def test_factorial_of_cero(self):
        number = 0
        fact = factorial_number(number)
        self.assertEqual(fact, 1)     

