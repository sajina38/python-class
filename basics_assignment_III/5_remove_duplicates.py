
def remove_duplicates(lst):
    remove_duplicates = []
    for item in lst:
        if item not in remove_duplicates:
            remove_duplicates.append(item)
    return remove_duplicates


print(remove_duplicates([1, 3, 3, 4, 1, 5]))  # Output: [1, 3, 4, 5]
