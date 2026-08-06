class Circle:
    def __init__(self,pie,radius):
        self.pie=pie
        self.radius=radius

    def AreaOfCircle(self):
        return self.pie*self.radius*self.radius
    
circle1=Circle(22/7,7)
print("The area of the circle is:",circle1.AreaOfCircle())
    