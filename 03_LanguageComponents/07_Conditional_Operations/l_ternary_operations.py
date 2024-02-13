#!/usr/bin/python3
"""
Purpose: Ternary operation usage

Useful, when there is  one condition and two ways
"""
num1 = 10

# Method 1
if num1 % 2 == 0:
    print("Even")
else:
    print("Odd")

# Method 2 - using ternary operation
# condition: successCase, failcase
print("Even" if num1 % 2 == 0  else "Odd")


if num1 == 0:
    print("Zero")
else:
    print("nonzero")

print("Zero" if num1 == 0 else "nonzero")


# num1 = 100
# num2 = 200
num1,  num2 = 100, 200   # tuple unpacking
if num1 == num2:
    print("num1 is equal to num2")
elif num1 > num2:
    print("num1 is greater")
else:
    print("num2 is greater")

# NOTE: ternary operations are suitable only for two cases scenarios

# Interview Questions
print((
    "num1 is equal to num2"  if num1 == num2 else
    (
        "num1 is greater" if num1 > num2 else "num2 is greater"
    )
))