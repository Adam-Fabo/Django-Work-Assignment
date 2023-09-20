# Simple script that checks all unique keys in a json file
# This script was made because checking element by element in a json file is tedious

import json
import pprint

f = open("test_data.json","r",encoding="utf8")
data = json.load(f)
f.close()


# Create empty dictionary to store unique keys
unique_keys = {}

# Iterate through data one element at a time
for element in data:

    # get element name
    element_name = list(element.keys())[0]

    # Check if element name is in unique_keys
    if element_name in unique_keys:
        # Add new keys to unique_keys and add to set new unique keys
        unique_keys[element_name] = unique_keys[element_name].union(set(element[element_name].keys()))

    else:
        # Add new element name to unique_keys, values are set of keys
        unique_keys[element_name] = set(element[element_name].keys())


# Pretty print unique keys
pprint.pprint(unique_keys)



