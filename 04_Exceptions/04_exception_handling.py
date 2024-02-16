#!/usr/bin/python3
"""
Purpose: Addition operation, with exception handling
    Importance of "else" block
"""

# Case 1 - without exception handling
# num1 = 1000
# num2 = 2022

# add_result = num1 + num2
# print(f"{add_result = }")


# num1 = 1000
# num2 = "2022"

# add_result = num1 + num2
# print(f"{add_result = }")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# try:
#     num1 = input("num1=")
#     num2 = input("num2=")
#     add_result = num1 + num2
# except Exception as ex:
#     print("Unhandled exception:", repr(ex))
# else:
#     print(f"{add_result = }")



# try:
#     num1 = int(input("num1="))
#     num2 = int(input("num2="))
#     add_result = num1 + num2
# except ValueError as vex:
#     print("Ensure that both inputs were integers only")
# except Exception as ex:
#     print("Unhandled exception:", repr(ex))
# else:
#     print(f"{add_result = }")



try:
    num1 = int(input("num1="))
    num2 = int(input("num2="))
    div_result = num1 / num2
except ZeroDivisionError as ex:
    print("Ensure that denomiator is always non-zero")
except ValueError as vex:
    print("Ensure that both inputs were integers only")
except Exception as ex:
    print("Unhandled exception:", repr(ex))
else:
    print(f"{div_result = }")
