#!/usr/bin/python3
"""
Purpose: Decorator for printing start and end of function

    A decorator is a function that allows us to wrap another function
    in order to extend the behavior of the wrapped function, without
    permanently modifying it.


"""


def addition(num1, num2):
    print("function -start ")
    result = num1 + num2
    print("function - before end")
    return result

def multiplication(num1, num2, num3):
    print("function -start ")
    result = num1 * num2 * num3
    print("function - before end")
    return result


print(addition(12, 34))
print(multiplication(12, 34, 10))
print()

# ==========================
# def print_function(func):
#     def inner(*args, **kwargs):
#         print("function -start ")
#         result = func(*args, **kwargs)
#         print("function - before end")
#         return result
#     return inner

def print_function(func):
    def inner(*args, **kwargs):
        print(f"{func.__name__} function - start ")
        result1 = func(*args, **kwargs)
        print(f"{func.__name__} function - before end")
        return result1

    return inner

@print_function
def addition(num1, num2):
    return num1 + num2

@print_function
def multiplication(num1, num2, num3):
    return num1 * num2 * num3


print(addition(12, 34))
print(multiplication(12, 34, 10))

