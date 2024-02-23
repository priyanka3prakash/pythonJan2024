#!/usr/bin/python3
"""
Purpose: Higher Order functions
    - function which were designed to work on another functions
    - zip, map, filter, reduce
    - NOTE: zip(), map() & filter() will ignore the asymmetric values in iterables
"""

group1 = ("1", "2", "3")
group2 = ("a", "b", "c", "d")

# result = zip(group1, group2) # <zip object at 0x7fd59cd74540>
result = list(zip(group1, group2) )# 
# NOTE: asymetric values will be ignored
print(result)       # [('1', 'a'), ('2', 'b'), ('3', 'c')]
print(dict(result)) # {'1': 'a', '2': 'b', '3': 'c'}
print()

result = zip(group2, group1)
print(dict(result))
print()

group3 = (True, False)
print(list(zip(group1, group2, group3)))  # [('1', 'a', True), ('2', 'b', False)]

# print(dict(zip(group1, group2, group3)))
# ValueError: dictionary update sequence element #0 has length 3; 2 is required


print(
    list(
        zip(
            (1, 2, 3),
            (11, 22, 33, 44),
            (111, 222, 333, 444),
        )
    )
)  # [(1, 11, 111), (2, 22, 222), (3, 33, 333)]
print()



# Question: How to make map to work like zip
print(list(zip((1, 2, 3), ["a", "b"])))
print(list(map(lambda x, y: (x, y), (1, 2, 3), ["a", "b"])))

# print(list(map(None, (1, 2, 3), ["a", "b"])))
# TypeError: 'NoneType' object is not callable

# ----------------------------


def is_positive(num):
    return True if num >= 0 else False


data = (12, -23.0, 2, -123, -0, 9)

print(list(map(is_positive, data)))

print(list(filter(is_positive, data)))
print()


# ----------------------------------------
# Caesar Cipher Implementation
print(list(map(lambda ch: ch, "Python")))
print(list(map(lambda ch: ord(ch), "Python")))
print(list(map(lambda ch: ord(ch) + 3, "Python")))
print(list(map(lambda ch: chr(ord(ch) + 3), "Python")))
print("".join(map(lambda ch: chr(ord(ch) + 3), "Python")))

# ----------------------------------------


def f1(x):
    return 3 * x


def f2(x):
    try:
        return x > 3
    except:
        return 0


data = [1, 2, 3, 4, 5, 6]
result = list(map(f1, filter(f2, data)))
print(result)