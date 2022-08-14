from math import factorial


def factorial_number(number):
    if number ==  (0 or 1):
        return 1
    else:
        return number * factorial(number-1)      