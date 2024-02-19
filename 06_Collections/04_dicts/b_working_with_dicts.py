#!/usr/bin/python3
"""
Purpose: Dictionaries
    - This is representation of the data structure
        - HashMap
    - Properties
        - represented using {} or dict()
        - from python 3.6 onwards, the order of dict is maintained
            - In older versions, OrderedDict module should be used for the same
        - Any data type can be used for dict values
        - dict keys should be immutables only
"""
from pprint import pp

alphabhets = {"b": 2, "a": 1, "c": 3, "d": 4}
print(alphabhets)

"""
In python < 3.6, use below code to retaining the assigned order

import OrderedDict
alphabhets = OrderedDict.OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(alphabhets)
"""

person_details = {
    "name": "Gudo Van Russom",
    "age": 67,
    "salary": 1233123.12,
    "children": ["mary", "John"],
    "parents": ("Sam Russom", "Michel Russom"),
    1: [12, 3, 12],
    -1213.213: {33, 33},
    ("Dr", "Mr"): "titles",
    None: "This is None",
    # [12, 23]: 'something',
    tuple([12, 23]): "something",
}
print(person_details)
print()

# pprint(person_details)
# pprint(person_details, indent=4)
# NOTE:
# 1. general print() will retain dict order
# 2. pprint() will sort by keys and display
# 3. pp() will retain dict order, as created.

# pp(person_details)
pp(person_details, indent=4)