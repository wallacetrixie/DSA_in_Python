class Student:

    university = "Co-operative University"

    def __init__(self, name):
        self.name = name


student1 = Student("Wallace")
student2 = Student("John")

print(student1.university)
print(student2.university)