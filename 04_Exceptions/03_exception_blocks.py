#!/usr/bin/python3
"""
Purpose: Exception Handling Blocks

    blocks - try, except, else, finally

    Execution Flow
        1. when no error     -> try -> else   -> finally
        2. when error occurs -> try -> except -> finally

NOTE: else and finally blocks are optional
NOTE:
    1. code which we may result in errors need to be placed in try block
    2. Error handling to corresponding errors need to be placed in except block
    3. If no errors in try block, corresponding actions in else block
    4. placeholder for all restrospective actions correspoding to that in try block
        ex: in try block, socket/file/remote_connect/db_connection was opened
            in finally block, we can close it

"""
# 10 / 0  # ZeroDivisionError: division by zero


try:
    10/0
except:
    pass

try:
    10/20
except:
    pass

# try:
#     num1 = input("Enter a number:")
#     print(2.5 * num1)
# except Exception as ex:
#     print(ex)
#     print(str(ex))
#     print(repr(ex))



# try:
#     num1 = input("Enter a number:")
# except Exception as ex:
#     print(repr(ex))
# else:
#     print(2.5 * num1)


# try:
#     num1 = input("Enter a number:")
# except Exception as ex:
#     print(repr(ex))
# except TypeError as tex:
#     print(repr(tex))
# else:
#     print(2.5 * num1)  # TypeError: can't multiply sequence by non-int of type 'float'



# Exception heierarcy - top to bottom left to right execution

# try:
#     num1 = input("Enter a number:")
#     res = 2.5 * num1
# except Exception as ex:
#     print("Unhandled exception:", repr(ex))
# except TypeError as tex:
#     print("ensure that num1 is of integer type:", repr(tex))
# else:
#     print(res)  


# try:
#     num1 = input("Enter a number:")
#     res = 2.5 * num1
# except TypeError as tex:
#     print("ensure that num1 is of integer type:", tex)
# except Exception as ex:
#     print("Unhandled exception:", repr(ex))
# else:
#     print(res)  


try:
    num1 = int(input("Enter a number:"))
    res = 2.5 * num1
except TypeError as tex:
    print("ensure that num1 is of integer type:", tex)
except ValueError as vex:
    print("Ensure that num1 is integer type only")
except Exception as ex:
    print("Unhandled exception:", repr(ex))
else:
    print(f"result is {res}")
finally:
    print("All done.. cleanup actions")