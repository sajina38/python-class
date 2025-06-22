
# Write a Python program to convert JSON data to Python object.

import json
json_data = '{"name": "Saji", "age": 20}'
python_object = json.loads(json_data)

print(python_object)
print(type(python_object))