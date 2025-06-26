class Vehicle:
    def __init__(self, name):
        self.name = name

    def start(self):
        return f"{self.name} suru bhayo"


class Jeep (Vehicle):
    def __init__(self, name, doors):
        super().__init__(name)
        self.doors = doors

    def honk(self):
        return "beep beep"


my_jeep = Jeep("BYD", 4)
print(my_jeep.start())
print(my_jeep.honk())
