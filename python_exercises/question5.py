# Write a Python program that creates all possible strings using the letters 
# 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.

import random

letters = ['a', 'e', 'i', 'o', 'u']

random.shuffle(letters)

print(''.join(letters))