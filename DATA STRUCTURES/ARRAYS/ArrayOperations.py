marks=[76,23,45,67,89,12,34,56,78,90]
#alternative is total=sum(marks)  fuction to sum all the marks in the list
total=0
for i in range(len(marks)):
    total+=marks[i]
print("Sum of all marks:", total)
