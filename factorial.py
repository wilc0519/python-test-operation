from math import factorial


def factorial_number(number):
    if number == 0:
        return 1

    if number == 1:
        return 1
    
    return number * factorial(number-1)      