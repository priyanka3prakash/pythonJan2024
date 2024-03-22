"""
Purpose: classes (OOP) introduction

    class - Blueprint ---- Rubber stamp
    Insta - replica    -- print of stamp is Instance

    classes
        1. old style classes - python 2
            class - type - class object
        2. new style classes - python 2 & 3

PEP 8 -> class names should be in CamelCasing
"""

# Function Definition
def hello():
    pass


# Function call
hello()
# ---------------------------------
# Class Definition


class EmptyClass:
    pass


# Class call - Instantiation
# - process for creating instance from a class
EmptyClass()

print(f"{type(EmptyClass) =}")  # <class 'type'>
print(f"{EmptyClass       =}")
print()

e1 = EmptyClass()
print(f"type(e1)        :{type(e1)}")  # <class '__main__.EmptyClass'>
print(f"e1              :{e1}")



# EmptyClass implicitly inherits from object
assert issubclass(EmptyClass, object) is True



class EmptyClass(object):
    pass


# EmptyClass implicitly inherits from object
assert issubclass(EmptyClass, object) is True