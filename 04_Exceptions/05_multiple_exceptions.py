"""
Multiple exceptions"""


# try:
#     num1 = int(input("num1="))
#     num2 = int(input("num2="))
#     div_result = num1 / num2
# except ZeroDivisionError as ex:
#     print("Ensure that denomiator is always non-zero")
# except ValueError as vex:
#     print("Ensure that both inputs were integers only")
# except Exception as ex:
#     print("Unhandled exception:", repr(ex))
# else:
#     print(f"{div_result = }")





# try:
#     num1 = int(input("num1="))
#     num2 = int(input("num2="))
#     div_result = num1 / num2
# except ArithmeticError as aex:
#     print("Arithmetic error - either of FloatingPointError, OverflowError or ZeroDivisionError occured")
# except ZeroDivisionError as ex:
#     print("Ensure that denomiator is always non-zero")
# except ValueError as vex:
#     print("Ensure that both inputs were integers only")
# except Exception as ex:
#     print("Unhandled exception:", repr(ex))
# else:
#     print(f"{div_result = }")



# try:
#     num1 = int(input("num1="))
#     num2 = int(input("num2="))
#     div_result = num1 / num2
# except ZeroDivisionError as ex:
#     print("Ensure that denomiator is always non-zero")
# except ArithmeticError as aex:
#     print("Arithmetic error - either of FloatingPointError, OverflowError or ZeroDivisionError occured")
# except ValueError as vex:
#     print("Ensure that both inputs were integers only")
# except Exception as ex:
#     print("Unhandled exception:", repr(ex))
# else:
#     print(f"{div_result = }")



try:
    num1 = int(input("num1="))
    num2 = int(input("num2="))
    div_result = num1 / num2
except (ZeroDivisionError, ArithmeticError, ValueError) as ex:
    print("Ensure that denomiator is always non-zero and \
           Ensure that both inputs were integers only")
except Exception as ex:
    print("Unhandled exception:", repr(ex))
else:
    print(f"{div_result = }")