from math import factorial


def factorial_number(number):
    if number ==  0:
        return 1
    else:
        return number * factorial(number-1)      