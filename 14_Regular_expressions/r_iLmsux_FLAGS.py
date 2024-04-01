"""
Purpose: Regular Expressions flags ?iLmsux
    i: tells the searching engine to ignore case
    L: makes \w, \b, and \s locale dependent
    m: enables multiline expression
    s: the dotall flag; it makes the dot match all characters, including newline character
    u: makes \w, \b, \d, and \s unicode dependent
    x: makes the expression verbose i.e. ignores unescaped whitespace as well as text after # sign i.e. it treats text after # as comments.
"""
import re

print("\n(?i)")
print(re.findall("hello", "Hello World", flags=re.IGNORECASE))
print(re.findall("hello", "Hello World", re.I))
print(re.findall("(?i)hello", "Hello World"))
print()

print("\n(?m)")
print(re.search('^P', 'Python\nis\nAwesome', re.MULTILINE)) 
print(re.search('^P', 'Python\nis\nAwesome', re.M)) 
print(re.search('(?m)^P', 'Python\nis\nAwesome')) 


print("\n(?s)")
print(re.search('P.*e', 'Python\nis\nAwesome', re.DOTALL))
print(re.search('P.*e', 'Python\nis\nAwesome', re.S))
print(re.search('(?s)P.*e', 'Python\nis\nAwesome'))


# (?x): Allows you to write more readable regular expressions by ignoring whitespace and comments.

import re
pattern = """
    ^              # Start of string
    \d{3}          # Exactly three digits
    -              # A dash
    \d{2}          # Exactly two digits
    -              # Another dash
    \d{4}          # Exactly four digits
    $              # End of string
"""
print(re.search(pattern, '123-45-6789'))
print(re.search(pattern, '123-45-6789', re.X))

pattern = """(?x)
    ^              # Start of string
    \d{3}          # Exactly three digits
    -              # A dash
    \d{2}          # Exactly two digits
    -              # Another dash
    \d{4}          # Exactly four digits
    $              # End of string
"""
print(re.search(pattern, '123-45-6789'))