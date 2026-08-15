# the colon before the number indicates we slice the first number of digits eg :4 the first four, colon after the digit
# collon after the digit means we skip the first 4, then we slice the rest after the first 4 eg 4:
marks=[32,22,88,63,87,33,7,33,38,89,56,23]
print(marks[:4]) #the first 4
print(marks[4:]) # th items after the first 4
print(marks[1:5]) #we skip  the first and 5th
print(marks[2:4]) #skip the first 2 and the last one
print(marks[::2]) #skips by 2 digits and we pick the second digit
print(marks[::3])# jumps by 3
print(marks[:-1]) #skips the last item/digit
print(marks[:-2]) #skips the last 2 items
print(marks[::-1]) #reverses the items in the list the last becomes the first one
