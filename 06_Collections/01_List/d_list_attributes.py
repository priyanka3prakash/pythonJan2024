#!/usr/bin/python3
# -*- coding: utf-8 -*-

mylist1 = [1, 11, 111, [11]]
print("mylist1       = ", mylist1)

mylist2 = [2, 22, 222]
print("mylist2       = ", mylist2)
print()


# list concatenation
newlist = mylist1 + mylist2
print("newlist       = ", newlist)
print("type(newlist) = ", type(newlist))
print()


print("commutative prop :", mylist1 + mylist2 == mylist2 + mylist1)
print("mylist1 + mylist2", mylist1 + mylist2)
print("mylist2 + mylist1", mylist2 + mylist1)


# Assignment: List repetition is commutative

# print(dir(mylist1))
for each_attribute in dir(mylist1):
    if not each_attribute.startswith('__'):
        # print(type(each_attribute), each_attribute) #, each_attribute.startswith('__'))
        print(each_attribute, end=',')
print()
# append,clear,copy,count,extend,index,insert,pop,remove,reverse,sort,


print(f"\n{mylist1             =}")
print(f"{mylist1.count(2)    =}")
print(f"{mylist1.count(11)   =}")
print(f"{mylist1.count([11]) =}")
print()

print(f"{mylist1[3]            =}") # list
print(f"{mylist1[3].count(11)  =}")
print(f"{mylist1[3].count([11])=}")

print(f"{mylist1[3][0]         =}") # int
# print(f"{mylist1[3][0].count(11)=}")
# AttributeError: 'int' object has no attribute 'count'
print()


print(f"\n{mylist1             =}")
