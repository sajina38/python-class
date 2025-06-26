
# #Parent class
class Animal ():
    def __init__(self, name):
        self.name = name

    def speak(self) -> str:
        return ""

# #Child class


class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"


class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"


dog = Dog("Max")
cat = Cat("Lily")
print(dog.speak())
print(cat.speak())
