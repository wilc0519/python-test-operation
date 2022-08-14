import unittest
from suma_numeros import sum_numbers, prod_numbers

class TestSuma(unittest.TestCase):
    def test_sum_numbers_default_args(self):
        sum = sum_numbers()
        self.assertEqual(sum,5050)


    def test_sum_number_given(self):
        numbers = (1,2,7)
        sum = sum_numbers(numbers)
        self.assertEqual(sum,10)
        self.assertEqual(sum_numbers(range(1,11)), 55)

    def test_prod_two_numbers(self):
        first_number = 4
        second_number = 7
        prod = prod_numbers(first_number, second_number)
        self.assertEqual(prod,28)

        

if __name__ == '__main__':
    unittest.main()