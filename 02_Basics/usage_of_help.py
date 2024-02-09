#!/usr/bin/python3
"""
Purpose: Demonstration of usage of help()
on python objects
"""

dozen = 12  # int
dozen = 12.3  # float
dozen = None  # NoneType
dozen = True  # bool
dozen = "True"

print("value   = ", dozen)
print("address = ", id(dozen))
print("type    =", type(dozen))
print("usage   =", dir(dozen))
print("documentaion=", dozen.__doc__)

# No print needed to display the help
# type q to exit the help
help(dozen)


# NOTE: help() usage differs only for string objects


print("=" * 40)
mountain = "Himalayas"  # string
print(f"{type(mountain) =}")
print(f"{id(mountain)   =}")
print(f"{mountain       =}")

print(f"{dir(mountain) =}")

help(mountain)
help(str)
help(mountain.isalpha)