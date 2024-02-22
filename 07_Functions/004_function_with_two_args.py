#!/usr/bin/python3
"""
Purpose: Functions Demo

    Function with two arguments and no return value
"""


# Function Definition
def hello(name, age):
    print(f"{name}'s age is {age}")


# Function call
# hello()
# TypeError: hello() missing 2 required positional arguments: 'name' and 'age'


# hello('Narender')
# TypeError: hello() missing 1 required positional argument: 'age'
    
# hello(27)
# TypeError: hello() missing 1 required positional argument: 'age'
    
print("\ncall By position")
hello('Narender', 27)
hello(27, 'Narender')

print("\ncall By keyword args")
hello(name='Narender', age=27)
hello( age=27, name='Narender')




def divisibility_test(m, n):
    if m % n == 0:
        print("%2d is divisible by     %2d" % (m, n))
    else:
        print("%2d is NOT divisible by     %2d" % (m, n))


divisibility_test(6, 9)
divisibility_test(6.0, 6)
divisibility_test(-6, 9.0)
divisibility_test(-6, -6)