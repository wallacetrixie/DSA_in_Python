marks=[34,87,87,56,33,23,56,76,98,2,87,90,45,73,87]
left=0
right=len(marks)-1
while left<right:
    marks[left],marks[right]=marks[right],marks[left]
    left+=1
    right-=1
print("The reversed array is:",marks)
