class Student:
    def __init__(details,name,age,action):
        details.name=name
        details.age=age
        details.action=action
    def Introduction(details):
        print("My name is:",details.name,"i am ",details.age,"years old","And i",details.action)
student1=Student("Wallace Wambulwa",22,"Love coding")
student1.Introduction()