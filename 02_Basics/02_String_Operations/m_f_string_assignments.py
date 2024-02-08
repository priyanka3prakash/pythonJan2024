#!/usr/bin/python3
"""
Purpose: F-String Assignments

        Introduced in python 3.8
"""
language = "Python"
print(language)
print("language", language)
print()

print("language =", language)
print("language = %s" % (language))
print("language = {}".format(language))
print(f"language = {language}")
print(f"{language = }")
print()

num = 1234
print(f"num = {num}")
print(f"{num = }")

# print(f'{NUmber =}')
# NameError: name 'NUmber' is not defined
print()

print("language :", language)
print(f"{language =}")
# print(f"{language -}") 
# SyntaxError: f-string: invalid syntax



print()

print(f"{num     = }")
print(f"{num     = }")
print(f"{num * 3 = }")
print(f"{num / 3 = }")
print(f"{num % 3 = }")