#!/usr/bin/python
"""
Purpose: Reading (parsing) multiple YAML docs
"""
import yaml

with open("data.yaml") as f:
    # Multiple YAML documents are read with load_all()
    docs = yaml.load_all(f, Loader=yaml.FullLoader)

    print(docs)
    for doc in docs:
        for k, v in doc.items():
            print(k, "->", v)