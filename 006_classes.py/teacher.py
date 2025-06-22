
class Teacher:
    total_teachers = 0  # Class variable

    def __init__(self, name):
        self.name = name
        Teacher.total_teachers += 1  # Increment when new teacher created

    @classmethod
    def get_total(cls):
        return f"Total teachers: {cls.total_teachers}"

# Create teachers
teacher1 = Teacher("Ram")
teacher2 = Teacher("Sita")
printTeacher.get_total())
