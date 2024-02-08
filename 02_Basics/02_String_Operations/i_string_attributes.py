#!/usr/bin/python3
"""
Purpose: String Attributes
"""
print("42".zfill(5))  # '00042'
print("-42".zfill(5))  # '-0042'


print("%05d" % (42))  # '00042'
print("%5d" % (42))  # '   42'
print("%+5d" % (42))  # '  +42'
print("%-5d" % (42))  # '42   '
print("%-05d" % (42))  # '42   '


print()
print("Python".center(25))
print("Python".center(25, "-"))
print("Python".center(25, "."))

print()
print("Python".ljust(25))
print("Python".ljust(25, "-"))
print("Python".ljust(25, "."))

print()
print("Python".rjust(25))
print("Python".rjust(25, "-"))
print("Python".rjust(25, "."))