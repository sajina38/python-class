
def filter_range(lst, min_val, max_val):
    filtered = []
    for num in lst:
        if min_val <= num and num <= max_val:
            filtered.append(num)
    return filtered


print(filter_range([1, 5, 3, 4, 2], 2, 5))
# Output: [5, 3, 4, 2]
