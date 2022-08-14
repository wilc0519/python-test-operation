import unittest
from suma_numeros import sum_numbers

class TestSuma(unittest.TestCase):
    def test_sum_numbers_default_args(self):
        sum = sum_numbers()
        self.assertEqual(sum,5050)


    def test_sum_number_given(self):
        numbers = (1,2,7)
        sum = sum_numbers(numbers)
        self.assertEqual(sum,10)
        self.assertEqual(sum_numbers(range(1,11)), 55)
        

if __name__ == '__main__':
    unittest.main()