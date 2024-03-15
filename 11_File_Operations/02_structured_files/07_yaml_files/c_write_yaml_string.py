#!/usr/bin/python

import yaml

users = [
    {"name": "John Doe", "occupation": "gardener"},
    {"name": "Lucy Black", "occupation": "teacher"},
]

print(yaml.dump(users))


my_dict = {"a": 1, "b": True, "c": False, "d": None}

# python object to yaml
yaml_string1 = yaml.dump(my_dict)
print(type(yaml_string1), '\n' +yaml_string1)


my_dict = {"a": 1, "b": True, "c": False, 
           "d": (None,), "e": {"name": "Gudo"}, 
           "f": ['Mango'],  "g": {1, 2, 3}}

# python object to yaml
yaml_string1 = yaml.dump(my_dict)
print(yaml_string1)


retrieved_data = yaml.load(yaml_string1, Loader=yaml.SafeLoader)
print(retrieved_data)

# Assignmen t - troubleshoot to address this issue 
# d: !!python/tuple