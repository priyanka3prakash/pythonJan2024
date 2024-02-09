#!/usr/bin/python3

import this

# print(this)

love = this

# is --- object level equivalence check
print(f"{this == love         =}")
print(f"{id(this) == id(love) =}")
print(f"{id(this)             =}")
print(f"{id(love)             =}")
print()


print(f"{this is love         =}")
# print(f'{this not is love         =}')
# SyntaxError: f-string: invalid syntax

print(f"{this is not love     =}")
print(f"{not this is love     =}")
print()

print(f"{this is love         =}")
print(f"{love is love         =}")
print(f"{love is not True or False=}")
print(f"{love is not (True or False)=}")  # PEDMAS


"""
is operator importance

    In [17]: val1 is val3
    Out[17]: True

    In [18]: val1 not is val3
    Cell In[18], line 1
        val1 not is val3
                ^
    SyntaxError: invalid syntax


    In [19]: val1 is not  val3
    Out[19]: False


"""