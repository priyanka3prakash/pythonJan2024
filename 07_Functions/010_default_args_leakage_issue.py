#!/usr/bin/python3
"""
Purpose: Functions with default args

    Memory leakage when mutable objects are taken as
    default arguments
"""
# anti-pattern
def extend_list(val, mylist=[]):
    print(f"\t{id(mylist)=} {mylist =}")
    mylist.append(val)
    return mylist

list1 = extend_list(123, [])
print(f"list1:{list1}")  # [123]

list2 = extend_list(10)
print(f"list2:{list2}")  # [10]

list3 = extend_list("a")
print(f"list3:{list3}")  # [10, 'a']

print(f"{id(list1) = }")  # 2472951626432
print(f"{id(list2) = }")  # 2472949383936
print(f"{id(list3) = }")  # 2472949383936

print("\n\nSolution when you need default list ==========")


def extend_list(val, mylist=None):
    # if not mylist:
    #     mylist = []
    mylist = mylist or []  # Boolean short-circuiting

    print(f"\t{id(mylist)=} {mylist =}")
    mylist.append(val)
    return mylist


list1 = extend_list(123, [])
print(f"list1:{list1}")  # [123]

list2 = extend_list(10)
print(f"list2:{list2}")  # [10]

list3 = extend_list("a")
print(f"list3:{list3}")  # ['a']

print(f"{id(list1) = }")  # 2057504399488
print(f"{id(list2) = }")  # 2057504373312
print(f"{id(list3) = }")  # 2057504399424