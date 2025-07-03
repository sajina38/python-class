
def centred_triangle():
    rows = 5
    for i in range(1, rows + 1):
        spaces = rows - i
        stars = 2 * i - 1
        print(" " * spaces + stars * "*")


def inverted_centred():
    rows = 5
    for i in range(rows, 0, -1):
        spaces = rows - i
        stars = 2 * i - 1
        print(" " * spaces + stars * "*")


centred_triangle()
inverted_centred()
