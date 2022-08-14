def sum_numbers(numbers = None):
    if numbers is None:
        return sum(range(1, 101))
    return sum(numbers)

def prod_numbers(number, number2):
    prod = number * number2
    return prod
