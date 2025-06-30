
#  Define function student_data() to print ID, name, and class if given

def student_data(student_id, student_name=None, student_class=None):
    print("Student ID:", student_id)
    if student_name:
        print("Student Name:", student_name)
    if student_class:
        print("Student Class:", student_class)


student_data(101, "Sajina", "BIT")
