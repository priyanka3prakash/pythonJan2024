#!/usr/bin/python3
"""
Purpose: String Module
"""
import string

print(string)
print(dir(string))

help(string)


# print(dir(string))
print(string.__doc__, end="\n\n")

print(f"{string.ascii_letters   =}")
print(f"{string.ascii_lowercase =}")
print(f"{string.ascii_uppercase =}")
print(f"{string.digits          =}")
print(f"{string.hexdigits       =}")
print(f"{string.octdigits       =}")
print(f"{string.printable       =}")
print(f"{string.punctuation     =}")
print(f"{string.whitespace      =}")
print()