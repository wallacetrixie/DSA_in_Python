class Animals():
    def __init__(self,name):
        self.name=name
    def Speak(self):
        print(self.name,"Is the animals name")

class Dog(Animals):
    def bark(self):
        print(self.name,"Barks")
dog1=Dog("FENNY")

dog1.bark()


