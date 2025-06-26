
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_even_dict = {}

for number in numbers:

    if number % 2 == 0:
        odd_even_dict[number] = "Even"

    else:
        odd_even_dict[number] = "Odd"


print(odd_even_dict)
