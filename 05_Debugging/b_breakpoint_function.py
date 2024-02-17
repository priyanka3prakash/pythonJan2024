#!/usr/bin/python
"""
Purpose: Debugging

TASK - To display all even numbers between 0 & 100

NOTE:
    ;(semi-colon) is statement separator
    breakpoint()
        - builtin function, introducted in python 3.6
        - same as import pdb; pdb.set_trace()
"""


# help(pdb)

# print(dir(pdb))

val_1 = int(input("Enter val_1      :"))
val_2 = int(input("Enter val_2      :"))
# print("val_1 =",val_1, val_2)

# import pdb; pdb.set_trace()
breakpoint()

# Multiplication
result = val_1 * val_2 # val_1 + val_2
print(f"Multiplication   :{result}")


# NOTE: ;(semi-colon) is statement separator