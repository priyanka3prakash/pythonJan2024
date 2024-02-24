#!/usr/bin/python3
"""
Purpose: closures in python
    - Closures can avoid the use of global values.
    - It provides some form of data hiding.
    - When there are few methods (one method in most cases) to be implemented in a
      class, closures can provide a better solution. But when the number of attributes
      and methods are more, it is better to implement a class.
    - It is a way of keeping alive a variable even when the function has returned.
      So, in a closure, a function is defined along with the environment.
      In Python, this is done by nesting a function inside the encapsulating function
      and then returning the underlying function.

"""

def outer():
    print("outer function - start ")

    def inner():
        print("inner function - start")
        return "something"

    # case 1:
    # inner()

    # case 2:
    # return inner()

    # case 3:
    return inner      


outer()

# inner()
# NameError: name 'inner' is not defined. Did you mean: 'iter'?


result = outer()
print(f"{type(result) = } {result =}")
print()

# <function outer.<locals>.inner

print(f"{result()  = }")
print(f"{outer()() = }")
