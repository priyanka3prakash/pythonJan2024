#!/usr/bin/python3
"""
Purpose: Demonstration of Palindrome check

    palindrome strings
        dad
        mom

        daddy -- NOT a palindrome

Algorithms:
-----------
Step 1: Take the string in run-time and store in a variable
"""
input_string = input("Enter any string:")
print("input_string   = ", input_string)

# reverse string
reverse_string = input_string[::-1]
print("reverse_string = ", reverse_string)

print(input_string == reverse_string)

if input_string == reverse_string:
    print(input_string, "is a palindrome")
else:
    print(input_string, "is not a a palindrome")
