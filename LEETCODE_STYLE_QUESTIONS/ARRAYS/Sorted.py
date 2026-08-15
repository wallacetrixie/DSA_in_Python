numbers=[21,34,78,23,21,56,76,43,87,75,3,9,34,44,59,21,83,76,37,87,37]
Sorted_marks=True
for i in range(len(numbers)-1):
    if numbers[i]>numbers[i+1]:
        Sorted_marks=False
        break
print(Sorted_marks)