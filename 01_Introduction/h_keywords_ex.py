#!/usr/bin/python3
"""
Purpose: keywords in python

    Reserved Keywords (35 in python 3.x)
    -------------------------------------
    False               class               from                or
    None                continue            global              pass
    True                def                 if                  raise
    and                 del                 import              return
    as                  elif                in                  try
    assert              else                is                  while
    async               except              lambda              with
    await               finally             nonlocal            yield
    break               for                 not

    
NOTE: These reserved keywords should not be used for the names of user-defined identifiers.

======================

variable
    keyword  -- variables defined by the language
    identifier  --- variables defined by user
                    or, user-defined variables


"""
# Loading a module
import keyword

print(keyword)
print(dir(keyword))  # uses
print()

print(keyword.kwlist)


print(True)  # True
# print(true)
# NameError: name 'true' is not defined. Did you mean: 'True'?

my_value = "something"
print(my_value)  # Identifier


# True = 'something'
# SyntaxError: cannot assign to True

true_value = 'something'


print(keyword.iskeyword("True")) # yes, it is a keyword
print(keyword.iskeyword("TrueValue")) # No, it is Not a keyword



# ------------------------------------------------------
# Identifiers - User-defined variables
#   - Naming Convention
#      1. keywords should not be used as identifiers
#      2. first character: a-z, A-Z, _
#      3. remaining chars: a-z, A-Z, _, 0-9


# ---- Rule 1
# True = 123  # SyntaxError: cannot assign to True
# None = 'Nothing'  # SyntaxError: cannot assign to None

true = 123
none = "Nothing"

# NOTE: PEP 8 - Dont create identifiers which are similar as Keywords
true_value = 123
none_result = "Nothing"

# ---- Rule 2 & 3
name = "Priyanka"
name_of_student = "Priyanka"
first_name = "Priyanka"
student_1 = "Priyanka"
class_02_a = "Python comment operations"
first_____child = "Satvik"

# PEP 8 recommends to use capitals for constants
PI = 3.1416
DOZEN = 12


# $name = "Priyanka"
# name-of-student = "Priyanka"
# name of student = "Priyanka"
# 1st_name = "Priyanka"  SyntaxError: invalid decimal literal#

_2nd_student = "someone"


_job = "software development"
__role = "Product support"
___salary = 1231231232312323233


# OOP -> name mangling
# variable   -> Public variable
# _variable  -> Protected variable
# __variable -> Private variable

# __variable__ ->  Built-in functions
# Ex: __file__, __name__, __doc__, __dict__, __init__

print("__name__ =", __name__)
print("__file__ =", __file__)


# print('__pavithra__ =', __pavithra__)
# # NameError: name '__pavithra__' is not defined