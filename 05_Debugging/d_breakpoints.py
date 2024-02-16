"""
breakpoints
"""

numbers = range(100)

import ipdb; ipdb.set_trace()

# To Display all even numbers
for each_num in numbers:
    if each_num % 2:
        print(each_num, end=", ")

