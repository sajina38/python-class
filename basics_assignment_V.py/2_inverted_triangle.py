
def inverted_triangle(num: int):
    for row in range(1, num + 1):
        for column in range(num, 0, -1):
            if column > 1:
                column = num - 1
                print(column * "*")


inverted_triangle(5)
