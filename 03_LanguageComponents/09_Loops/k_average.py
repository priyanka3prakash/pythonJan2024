#!/usr/bin/python
"""
Purpose: Calculating the average for the
    inputted numbers in run-time
"""

result = eval("1")
print(f"{result =} {type(result)}")  # int


result = eval("123.23")
print(f"{result =} {type(result)}")  # float

# result = eval("123 23")
# SyntaxError: invalid syntax

result = eval("12 + 23/32 * 23")
print(f"{result =} {type(result)}")  # float

# result = eval('Apple')
# NameError: name 'Apple' is not defined. Did you mean: 'tuple'?

# result = eval("Apple")
# NameError: name 'Apple' is not defined. Did you mean: 'tuple'?

result = eval('"Apple"')
print(f"{result =} {type(result)}")  # str

result = eval("'Apple'")
print(f"{result =} {type(result)}")  # str

Mango = 12
result = eval('Mango')
print(f"{result =} {type(result)}")  # int

result = eval("Mango")
print(f"{result =} {type(result)}")  # int


Apple = 12132
result = eval("Apple")
print(f"{result =} {type(result)}")  # int


# Assignment - calculate the avergae of numbers provided in runtime
# HINTS - while , input(), eval(), len(), sum()