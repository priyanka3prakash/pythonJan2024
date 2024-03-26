"""
Purpose: constructor is a method which will be
    called the moment instance is created


    functions vs methods
        methods - are kind of functions defined in classes

        methods -- Need to be called explicitly
        constructor is only methods which will be called implicitly on creating instance
    
        self - acts as a placeholder for the instance being passed

        contrcutor method can return only None
"""
from pprint import pp

class Person:

    def __init__(self):
        print("New instance is born! Adding default features")
        variable = 'local variable'
        self.variable = 'instance variable'
        self.name = 'Person1'
        self.age = 30

    def instance_method(self):
        return "This is an instance method"

# Instantiation
p1 = Person()
print(p1)

print(Person.instance_method(p1))
print(p1.instance_method())
assert p1.instance_method() == Person.instance_method(p1)

# p1.__init__() # But NOT RECOMMEND, as code duplicate execution


for each_attribute in dir(p1):
    print(each_attribute)

print()


# To get only the instance variables
print(f"p1.__dict__: {p1.__dict__}")
print(f"vars(p1)   : {vars(p1)}")
assert vars(p1) == p1.__dict__
print()



print("vars(Person):")
pp(vars(Person))
print()
# -------------------------------------------------

pp(vars())  # pp(globals())

# Note: calling the vars() function without parameters will
# return a dictionary containing the local symbol table.


"""
Assignment:
    run below in shell
    vars(list)
    vars(str)
    vars(dict)
"""