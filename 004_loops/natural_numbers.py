def natural_numbers():

    num = int(input("Enter a number: "))
    sum = 0

    for i in range(0, num + 1):
        sum += i

    print(sum)

    natural_numbers()
