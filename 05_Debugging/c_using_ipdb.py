#!/usr/bin/python
"""
Purpose: Debugging with ipdb

TASK - To display all even numbers between 0 & 100

To install ipdb,
    pip install -U ipdb --user

NOTE: TO make ipdb as the default, when using breakpoint(),
    export PYTHONBREAKPOINT='ipdb.set_trace'

"""


# help(pdb)

# print(dir(pdb))

val_1 = int(input("Enter val_1      :"))
val_2 = int(input("Enter val_2      :"))
# print("val_1 =",val_1, val_2)

# import pdb; pdb.set_trace()
# breakpoint()
import ipdb; ipdb.set_trace()

# Multiplication
result = val_1 * val_2 # val_1 + val_2
print(f"Multiplication   :{result}")


# NOTE: ;(semi-colon) is statement separator