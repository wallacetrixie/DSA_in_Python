numbers=[21,34,78,23,21,56,76,43,87,75,3,9,34,44,59,21,83,76,37,87,37]
results=[]
for i in range(len(numbers)):
    if numbers[i] not in results:
        results.append(numbers[i])      
print("Array without dupplicates:",results)

   
