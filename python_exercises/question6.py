# Write a Python program to make combinations of 3 digits.
import itertools

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

combinations = itertools.combinations(digits, 3)

for combo in combinations:
    print(''.join(combo))