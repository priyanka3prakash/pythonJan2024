#!/usr/bin/python3
"""
Purpose: Higher Order Functions
            - reduce
            - bulitin function in python 2.x
            - part of functools module in python 3.x

"""
from functools import reduce
import itertools

print(list(map(lambda x: x * 2, [1, 2, 3, 4])))

# print(list(map(lambda x, y: x + y, [1, 2, 3, 4])))
# TypeError: <lambda>() missing 1 required positional argument: 'y'
# For map(), if we have two args in function, we need to give two iterables

print(list(map(lambda x, y: x + y, [1, 2, 3, 4], (11, 22, 33))))
print(list(map(lambda x, y: x + y, "abcd", "zyx")))

# print(list(map(lambda x, y, z: x + y, 'abcd', 'zyx', [1, 2, 3])))
# TypeError: can only concatenate str (not "int") to str

print(list(map(lambda x, y, z: x + y, "abcd", "zyx", [1, 2, 3])))
print(list(map(lambda x, y, z: x + y + str(z), "abcd", "zyx", [1, 2, 3])))
print()


print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))  # (((1+2)+3)+4)
# NOTE: reduce() will take a single iterable only
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))  # factorial(4)
print(reduce(lambda x, y: x * y, range(1, 4 + 1)))  # factorial(4)

print(reduce(lambda x, y: x**y, [1, 2, 3, 4]))  # # (  ( (1 ** 2)) ** 3 ) ** 4
print(reduce(lambda x, y: x**y, [2, 3, 4]))
# -----------------------------------------------------------


def my_factorial(given_num):
    result = 1
    for each_num in range(1, given_num + 1):
        # result = result * each_num
        result *= each_num
    return result


print(my_factorial(9))


print(reduce(lambda num1, num2: num1 * num2, range(1, 9 + 1)))


# -------------------------------------------------------------
import operator
# print(dir(operator))


print(reduce(lambda a, b: a + b, [1, 3, 5, 6, 2]))
print(reduce(operator.add, [1, 3, 5, 6, 2]))


print(reduce(lambda a, b: a * b, [1, 3, 5, 6, 2]))
print(reduce(operator.mul, [1, 3, 5, 6, 2]))


mystrings = ("I", "am", "confident", "about", "myself")
print(reduce(operator.add, mystrings))
print(reduce(lambda word1, word2: word1 + " " + word2, mystrings))



# ---------------------------------------------------------------

# to get the intermediate values, using reduce operation
print(reduce(lambda p, q: p + q, [1, 3, 5, 6, 2]))  # 17
print(reduce(operator.add, [1, 3, 5, 6, 2]))  # 17
print(
    list(itertools.accumulate([1, 3, 5, 6, 2], lambda x, y: x + y))
)  # [1, 4, 9, 15, 17 ]
print()


"""
Assignment: mimick sum() builtin function with
 a. user-defined function
 b. using reduce
"""
print(sum((1, 23, 23, 2)))
print(sum([(1, 2), (3,), (9, 1)], ()))
print(sum([[1, 2], [3, 4]], []))