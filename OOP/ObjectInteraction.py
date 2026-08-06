class Rectangle:
    def __init__(details,length,width):
        details.length=length
        details.width=width
    def Area(details):
        print("The length is:",details.length,"and the width is",details.width)
        print("The area of the rectangle is:",details.length*details.width)
area1=Rectangle(10,20)
area1.Area()