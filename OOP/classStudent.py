class Student:
    def __init__(details,name,age,course):
        details.name=name
        details.age=age
        details.course=course
student1=Student("Wallace Wambulwa",22,"Information Technology")
student2=Student("Mary kioko",21,"Software Engineering")
print(student1.name,student1.age,student1.course)
print(student2.name,student2.age,student2.course)

