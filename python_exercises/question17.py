# Write a Python script to merge two Python dictionaries.

d1 = {'a': "cat", 'b': "dog"}

d2 = {'x': "tiger", 'y': "kangaroo"}


d = d1.copy()

d.update(d2)

print(d)
