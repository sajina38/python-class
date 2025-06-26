# class bhitra return cha bhaney tala call garni bela print
# class bhitra print garisakyo bhaney call matra garni last ma


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")


manager1 = Manager("Yuna", 40000, "HA")
manager1.details()

manager2 = Employee("Sarah", 50000)
manager2.details()
