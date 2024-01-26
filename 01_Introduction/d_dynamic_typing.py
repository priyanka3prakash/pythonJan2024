#!/usr/bin/python3
"""
Purpose: Python is a dynamic Typed Language.
    Progamming Languages
        - Classficiation
            1. Static-Typed Languages (c, c++, java)
                - first declare the variables, &
                - then use them
                    int a, float b  # Declaration
                    a = 10          # initialization

            2. Dynamic Typed Languages (python, perl, ruby)
                 - create when you need. No declaration needed
                    num1 = 123
                    num2 = 123.4
                    num2 = None
"""
num1 = 100

type(num1)
print(type(num1))


print(num1)
print("num1")

print("num1", num1)
print("num1 =", num1)

print("num1 =", num1, "type(num1) =", type(num1))

num1 = 300
print("num1 =", num1, "type(num1) =", type(num1))


# Python is a dynamic-typed language
num1 = 300.0
print("num1 =", num1, "type(num1) =", type(num1))

num1 = 300.
print("num1 =", num1, "type(num1) =", type(num1))

num1 = 300,
print("num1 =", num1, "type(num1) =", type(num1))

num1 = 300j
print("num1 =", num1, "type(num1) =", type(num1))

num1 = "300"
print("num1 =", num1, "type(num1) =", type(num1))
print()

num1 = None
print("num1 =", num1, "type(num1) =", type(num1))


num1 = True
print("num1 =", num1, "type(num1) =", type(num1))


num1 = False
print("num1 =", num1, "type(num1) =", type(num1))


num1 = "False"
print("num1 =", num1, "type(num1) =", type(num1))

# NOTE: Strings need to be declared in quotes