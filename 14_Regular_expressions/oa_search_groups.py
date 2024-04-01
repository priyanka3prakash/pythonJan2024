"""
purpose: regular expression

"""

import re

print(re.search("[a-z]+", "Udhay Prakash").group())
print(re.search("[a-zA-Z0-9]+", "Udhay Prakash").group())
print(re.search(r"\w+", "Udhay Prakash").group())
print()

print(re.search(r"\w+\W\w", "Udhay Prakash").group())
print(re.search(r"\w+\W\w+", "Udhay Prakash").group())
print()

print(re.search(r"\w+\s\w+", "Udhay Prakash").group())
print(re.search(r"\S+\s\S+", "Udhay Prakash").group())
print()

# Grouping in regular expressions
print(re.search(r"(\w+)\s(\w+)", "Udhay Prakash").group())
print(re.search(r"(\w+)\s(\w+)", "Udhay Prakash").group(0))
#                  1       2
print(re.search(r"(\w+)\s(\w+)", "Udhay Prakash").group(1))  # Udhay
print(re.search(r"(\w+)\s(\w+)", "Udhay Prakash").group(2))  # Prakash
print()

# print(re.search(r"(\w+)\s(\w+)", "Udhay Prakash").group(5)) 
# IndexError: no such group


print(re.search(r"(\w+)\W(\w+)", "Udhay Prakash").groups())
# ('Udhay', 'Prakash')

print(re.search(r"(\w+)(\W)(\w+)", "Udhay Prakash").groups())
# ('Udhay', ' ', 'Prakash')
