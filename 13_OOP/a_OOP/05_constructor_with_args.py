"""
Purpose: Constructor with args
"""


# class definition
class Animal:
    def __init__(self, name):
        self.name = name
        print(f'New animal {self.name} is born!!!')

    def walk(self):
        print(self.name + " walks.")



if __name__ == "__main__":
    # Instantiation

    # Animal()
    # TypeError: Animal.__init__() missing 1 required positional argument: 'name'

    Animal("Duck")
    duck1 = Animal("Duck")

    # Animal.__init__(duck1, "Duck")
    # NOT RECOMMENDED

    print(dir(duck1))
    print(vars(duck1))

    # calling instance method
    duck1.walk()

        # -------------------
    rhino = Animal("African Rhino")
    rhino.walk()

    # TO retrieve the instance variables
    print(vars(rhino))
    print(f"rhino.name:{rhino.name}")