#!/usr/bin/python3
"""
Purpose: Solving problem without decorators
"""


# def add(a, b):
#     return a + b

# def div(n1, n2):
#     return n1 / n2

def add(a, b):
    try:
        result = a + b
    except Exception as ex:
        return ex
    else:
        return result


def div(n1, n2):
    try:
        result = n1 / n2
    except Exception as ex:
        return ex
    else:
        return result


print(add(12, 34))
print(add("12", "34"))
print(add(12, "34"))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(add("12", 34))

print()

print(div(10, 5))
print(div(0, 5))
print(div(5, 0))  # ZeroDivisionError: division by zero