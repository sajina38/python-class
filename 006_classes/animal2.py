
# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def intro(self):
#         print(f"My name is {self.name}")
#         print("inside intro method")
#         print("self", self)


# a = Animal("Coco")
# a.intro()

# print("Outside class")
# print(a)

# from os import name


class Student:

    def __init__(self, name, roll_num):
        self.name = name
        self.roll_num = roll_num

    def show(self):
        print(f"The student's name is {self.name} and her roll number is {self.roll_num}")


s1 = Student("Sajina", 1)
s1.show()
