
# Write a Python program to convert Python dictionary object (sort by key)
# to JSON data. Print the object members with indent level 4.
import json

data = {'b': "rabbit", 'a': "cat", 'c': "dog"}

json_output = json.dumps(data, sort_keys=True, indent=4)

print(json_output)