"""
Purpose: Regular Expressions
    Using re.match
        - It helps to identify patterns at the starting of string
    Using re.search
        - It helps to identify patterns at the ANYWHERE of string

"""
import re

# print(dir(re))

target_string = "Python Programming is good for health"
# search_string = "python"

for search_string in ("python", "Python", "PYTHON", "PYThon"):
    print("\nsearch_string =", search_string)

    print(f"{target_string.find(search_string) =}")
    print(f"{search_string in target_string    =}")
    print()

    reg_obj = re.compile(search_string, re.IGNORECASE) # re.I
    print(reg_obj, type(reg_obj))

    # result = reg_obj.match(target_string)
    # .match can get only at the starting of string

    result = reg_obj.search(target_string)
    # .search - can get any where in the string, including starting
    print(f"{result =}")

    if result:
        print(f"result.group():{result.group()}")
        print(f"result.span() :{result.span()}")
        print(f"result.start():{result.start()}")
        print(f"result.end()  :{result.end()}")
    else:
        print("NO match found")