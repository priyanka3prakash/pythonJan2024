#!/usr/bin/python
"""
Methods
    1. Instance Methods -- will have self
    2. class Methods --- will have cls
    3. static Methods --- Nothing

Default Decorators: @staticmethod, @classmethod, @property
"""
# class MyClass:
#     my_var = "something"  # class variable

#     def display(self, x):
#         print("executing instance method display(%s,%s)" % (self, x))

    
#     def cmDisplay(cls, x):
#         print("executing class method display(%s,%s)" % (cls, x))
    
#     cmDisplay = classmethod(cmDisplay)

#     def smDisplay(x):
#         print("executing static method display(%s)" % x)
#         # neither use instance methods, instance variable, class methods nor class variables
    
#     smDisplay = staticmethod(smDisplay)



class MyClass:
    my_var = "something"  # class variable

    def display(self, x):
        print("executing instance method display(%s,%s)" % (self, x))

    @classmethod
    def cmDisplay(cls, x):
        print("executing class method display(%s,%s)" % (cls, x))

    @staticmethod
    def smDisplay(x):
        print("executing static method display(%s)" % x)
        # neither use instance methods, instance variable, class methods nor class variables


if __name__ == "__main__":
    a = MyClass()

    a.display("Django")             # accessing instance method
    MyClass.display(a, "Django")    # accessing instance method

    a.cmDisplay("Django")           # accessing class method
    MyClass.cmDisplay("Django")     # accessing class method

    a.smDisplay("Django")           # accessing static method
    MyClass.smDisplay("Django")     # accessing static method




class Myclass:
    val = 2

    def __init__(self):
        self.val = 0

    @staticmethod
    def incr(val):
        return val + 1
    
    def increment(self):
        self.val = self.incr(self.val)

I = Myclass()
print(f"{I.val = }")

print(I.incr(10))

print(f"{I.val = }")
