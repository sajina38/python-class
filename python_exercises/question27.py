# Write a Python program to create two empty classes, Student and Marks. Now create some
# instances and check whether they are instances of the said classes or not. Also, check whether
# the said classes are subclasses of the built-in object class or not.


class Student:
    pass


class Marks:
    pass


s = Student()
m = Marks()

print(isinstance(s, Student))         # True
print(isinstance(m, Marks))           # True
print(issubclass(Student, object))    # True
print(issubclass(Marks, object))      # True
