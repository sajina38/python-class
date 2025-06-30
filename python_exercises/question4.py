# Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.

def unique_numbers(sequence):
    if len(sequence) == len(set(sequence)):
        return True
    else:
        return False


print(unique_numbers([2, 4, 5, 8]))
print(unique_numbers([2, 2, 5, 8]))
