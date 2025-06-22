# Write a Python program to access only unique key value 
# of a Python object.

data = {
    "name": "Sajina",
    "age": 20,
    "friend": "Jharana",
    "college": "ICP",
    "age": 20
}

unique_keys = data.keys()
print("The unique keys are:", list(unique_keys))