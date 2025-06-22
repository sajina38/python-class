
# Write a Python program to filter a dictionary based on values.

marks = {'Sajina Gurung': 175, 'Jharana Gurung': 180, 'Suman Thapa': 165, 'Sujina Thapa': 190}

print("Original Dictionary:")
print(marks)

print("Marks greater than 170:")

result = {key: value for (key, value) in marks.items() if value >= 170}

print(result)
