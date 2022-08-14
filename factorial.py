from math import factorial


def factorial_number(number):
    if (number == 0 or  number == 1)  :
        return 1
    
    return number * factorial(number-1)      