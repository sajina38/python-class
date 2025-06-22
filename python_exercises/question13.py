# Write a Python program to create a list by concatenating a given 
# list with a range from 1 to n.

chars = ['p', 'q']
n = 5
result = []

for i in range(1, n + 1):
    for ch in chars:
        result.append(ch + str(i))

print(result)
