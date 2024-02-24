#!/usr/bin/python3
"""
Purpose: closure example demo
"""


def outer(num1):
    num3 = 30

    def hello_world():
        print("Hello world")

    def wrapper(num2):  # closure function
        result = num1 + num2 + num3
        return result
    

    print(f"\n{hello_world.__closure__ =}")
    print(f"{wrapper.__closure__ =}")

    if num1 % 2 == 0:
        return wrapper
    else:
        return hello_world
    
print(f"{outer(10) =}") # <function outer.<locals>.wrapper at 0x7f04e33931c0>
print(f"{outer(11) =}") # <function outer.<locals>.hello_world at 0x7f8bb46cf1c0>

print(f"{outer.__closure__ =}")
