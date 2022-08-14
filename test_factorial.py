import unittest
from suma_numeros import sum_numbers, prod_numbers

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        number = 3
        self.assertEqual(number, 6)

