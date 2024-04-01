"""
Purpose: Regular Expressions
    Using re.match
        - It helps to identify patterns at the starting of string
    Using re.search
        - It helps to identify patterns at the ANYWHERE of string

"""
import re

target_string = "Programming is good in PyTHOn"
search_string = "python"

print(f"{target_string.lower().find(search_string.lower()) =}")
print(f"{search_string.lower() in target_string.lower()    =}")
print()

regobj = re.compile(search_string, re.I)

for target_string in (
    "Python Programming is good",
    "Programming is Python is good",
    "Programming is good in PyTHOn",
):
    print("\n target_string",target_string )
    print("re.match :", regobj.match(target_string))
    print("re.search:", regobj.search(target_string))
          

