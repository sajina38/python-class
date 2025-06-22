
# Write a Python program to generate all sublists of a list.

def all_sublists(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            result.append(lst[i:j])
    return result

    print(all_sublists([1, 2, 3]))
