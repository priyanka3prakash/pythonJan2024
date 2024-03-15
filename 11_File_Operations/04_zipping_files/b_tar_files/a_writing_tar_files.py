"""
Purpose: Working with tar files
"""

import os
import tarfile


# if not os.path.exists('files'):
#     os.mkdir('files')

os.makedirs('files', exist_ok=True)
os.chdir('files')


# creating files
open("fileOne.txt", "w").write("This is first line\n")
open("fileTwo.txt", "w").write("This is second line\n")
open("fileThree.txt", "w").write("This is third line\n")

# Creating new archives
with tarfile.open("tarFileOne.tar", mode="w") as tF:
    tF.add("fileOne.txt")
    tF.add("fileTwo.txt")

# Appending to existing archive
with tarfile.open("tarFileOne.tar", mode="a") as tF:
    tF.add("fileThree.txt")



# deleting existing files
os.remove("fileOne.txt")
os.remove("fileTwo.txt")
os.remove("fileThree.txt")


# linux command to extract tar files: tar -xvf tarFileOne.tar