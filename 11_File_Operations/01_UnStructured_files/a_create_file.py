#!/usr/bin/python
"""
Purpose:
    file operations
        - read  - r
        - write - w -> if file not present, file will be created;
                       if present, existing content will be overwritten
        - append- a

        default is read mode

"""
# open()
# TypeError: open() missing required argument 'file' (pos 1)


# open('a_first_file.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'a_first_file.txt'


# open(file='a_first_file.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'a_first_file.txt'

# open(file='a_first_file.txt', mode='r')
# FileNotFoundError: [Errno 2] No such file or directory: 'a_first_file.txt'

# open(file='a_first_file.txt', mode='w')

file_handler = open("a_first_file.txt", mode="w")
print(f"{type(file_handler) =}")  # <class '_io.TextIOWrapper'>
print(f"{file_handler       =}")


file_handler = open("a_first_file.txt", mode="w", encoding="utf-8")
print(f"{file_handler       =}")


# To add content to file
file_handler.write("This is the first line\n")
file_handler.write("This is the second line\n")

# To close the file handler
file_handler.close()


# file_handler.write("This is the third line\n")
# ValueError: I/O operation on closed file.
