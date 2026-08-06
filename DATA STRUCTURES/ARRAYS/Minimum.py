def Smallest(marks):
    minimum=marks[0]
    for i in range(len(marks)):
        if marks[i]< minimum:
            minimum=marks[i]
    return minimum
marks=[34,55,66,34,5,67,23,77]
print("The smallest marks is:",Smallest(marks))
        
