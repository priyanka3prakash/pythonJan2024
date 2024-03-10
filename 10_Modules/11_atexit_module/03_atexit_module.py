#!/usr/bin/python
"""
Purpose: Exceptions in atexit Callbacks

"""
import atexit


def exit_with_exception(message):
    raise RuntimeError(message)


atexit.register(exit_with_exception, "Registered first\n")
atexit.register(exit_with_exception, "Registered second\n")
atexit.register(exit_with_exception, "Registered third\n")



# Assignment: create a function, where with while loop, code executes infinte time. 
# ctrl + c, and see if the atexit is helpful

