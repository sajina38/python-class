
def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)

    return inverted


print(invert_dict({"a": 1, "b": 2, "c": 1, "d": 3}))
# Output: {1: ['a', 'c'], 2: ['b'],
