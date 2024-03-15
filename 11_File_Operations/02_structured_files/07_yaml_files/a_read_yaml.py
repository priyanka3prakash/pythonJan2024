#!/usr/bin/python
"""
Purpose: Reading (Parsing) YAML files
    YAML
        - YAML Ain't Markup Language
        - human-readable data-serialization language.
        - commonly used for configuration files,
        - also, in data storage (e.g. debugging output) or transmittion (e.g. document headers)

        - natively supports three basic data types:
            1. scalars (such as strings, integers, and floats),
            2. lists, and
            3. associative arrays.

    Installation
        pip install -U pyyaml --user
"""
from pprint import pp
import yaml

# print(dir(yaml))

with open('person.yaml', 'r') as fh:
    # person_data = yaml.load(fh, Loader=yaml.SafeLoader)
    person_data = yaml.safe_load(fh)


pp(person_data)