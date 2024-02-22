#!/usr/bin/python3
"""
Purpose: Functions Demo

    Function with two arguments and default return value
NOTE: return is the last statement in function execution

"""


# Function Definition
def addition(n1, n2):
    # return "Hello world"
    # return
    # return None
    # return "None"
    # return "None",
    # return 123
    # return 123.
    # return 123.,
    # return 123.,,  SyntaxError: invalid syntax
    # return (123.,),
    return 12 - 123 * 23 / 3 // 23


# Function call
addition(12, 13)

answer = addition(12, 13)
print(type(answer), answer)


# NOTE:
# 1. By default, function return is None
# 2. return is the last executing statement in a function