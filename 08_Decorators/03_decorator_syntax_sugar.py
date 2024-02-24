#!/usr/bin/python3
"""
Purpose: Creating Exception Handling Decorator
    - writing generic decorator with variable args & keyword args handling
"""

def exception_handling(func):  # -> Decorator function
    # def inner(v1, v2, v3=0):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs) # v1, v2, v3)
            # print(f'{func =}')
        except Exception as ex:
            return ex
        else:
            return result

    return inner

def div(n1, n2):  # 2 arguments
    return n1 / n2

div_with_excp = exception_handling(div) # consuminption 
print(f"{div_with_excp(10, 12) =}")
print(f"{div_with_excp(0, 12) =}")
print(f"{div_with_excp(10, 0) =}")


@exception_handling                   # defnition side 
def div(n1, n2):  # 2 arguments
    return n1 / n2

print(f"{div(10, 12)=}")
print(f"{div(0, 12)=}")
print(f"{div(10, 0)=}")


#======================================

def addition(n1, n2, n3):
    return n1 + n2 + n3

add_with_excp = exception_handling(addition)
print(f"{add_with_excp(10, 20, 30) = }")
print(f"{add_with_excp(10, 20, '30') = }")
print(f"{add_with_excp(10, '20', 30) = }")

@exception_handling
def addition(n1, n2, n3):
    return n1 + n2 + n3

print("{addition(10, 20, 30) =}")
print("{addition(10, 20, '30') =}")
print("{addition(10, '20', 30) =}")