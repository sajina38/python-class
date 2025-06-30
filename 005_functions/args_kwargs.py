
# def add(*add_arguments):
# def multiply(*args):

#     product = 1

#     for item in args:
#         product = product * item

#     print(product)


# multiply(2, 8, 4, 9)


def greet(**kwargs):

    for value in kwargs.values():
        print(value)


greet(first_name="Sajina", middle_name="crazy", last_name="Gurung")


# def greeting(*kwargs):
#     first_name = kwargs.get("first_name")
#     last_name = kwargs.get("last_name")
#     middle_name = kwargs.get("middle_name")
#     print("My name is {name}")
