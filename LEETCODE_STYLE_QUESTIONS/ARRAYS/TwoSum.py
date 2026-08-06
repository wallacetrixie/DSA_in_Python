numbers=[21,34,78,23,21,56,76,43,87,75,3,9,34,44,59,21,83,76,37,87,37]
target=12

for i in range(len(numbers)):
    for k in range(i+1,len(numbers)):
        if numbers[i]+numbers[k]==target:
            print("The sum of the numbers that add to:",target,"are ",numbers[i],"and",numbers[k])
            print([i,k])