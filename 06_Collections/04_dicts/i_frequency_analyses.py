#!/usr/bin/python3
"""
Purpose: Test Frequency Analyses
"""

sentence = """Python is a wonderful language.
we can solve any
computational problem with this language"""


# Character frequency analyses
# Method 1
frequency = {}
for each_char in sentence:
    # print(each_char)
    # frequency[each_char] = 1
    try:
        frequency[each_char] = frequency[each_char] + 1
    except KeyError:
        frequency[each_char] = 1
print(frequency)


# Method 2
frequency = {}
for each_char in sentence:
    if each_char in frequency: # key is present
        frequency[each_char] = frequency[each_char] + 1
    else:
        frequency[each_char] = 1
print(frequency)


# Method 3
frequency = {}
for each_char in sentence:
    # frequency[each_char] = frequency[each_char] + 1
    frequency[each_char] = frequency.get(each_char, 0) + 1
print(frequency)


# Method 4
frequency = {}
for each_char in sentence:
    frequency.setdefault(each_char, 0)
    # frequency[each_char] = frequency[each_char] + 1
    frequency[each_char] += 1
print(frequency)
