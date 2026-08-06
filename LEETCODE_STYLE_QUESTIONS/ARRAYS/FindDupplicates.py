numbers=[21,34,78,23,21,56,76,43,87,75,3,9,34,44,59,21,83,76,37,87,37]
seen=set()
dupplicate=set()
for i in range(len(numbers)):
    if numbers[i] in seen:
        dupplicate.add(numbers[i])
    else:
        seen.add(numbers[i])
print(list(dupplicate))