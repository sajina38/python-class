
def multiply(numbers):
    # variable 'total' to store the multiplication result, starting at 1
    total = 1

    for x in numbers:
        # Multiply the current element 'x' with the 'total'
        total *= x

    return total

    print(multiply((8, 2, 3, -1, 7)))
