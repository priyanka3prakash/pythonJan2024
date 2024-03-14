#!/usr/bin/python
"""
Purpose: Reading(Parsing) csv, using unstructure file ops
"""
# Method 1
with open("my_file.csv", mode="r") as fh:
    file_content = fh.read()
    # print(file_content)

names = []
for line in file_content.splitlines()[1:]: #  .split('\n'):
    if line:
        names.append(line.split(',')[1])

print(f"{names =}")


# Assignment : try with fh.readlines(), instead of fh.read()
# Assignment: try with fh.readline(), with a yield to create like a generator
