numbers=[21,34,78,23,21,56,76,43,87,75,3,9,34,44,59,21,83,76,37,87,37]
target=90
for i in range (len(numbers)):
    for k in range(i+1,len(numbers)):
        for j in range(k+1,len(numbers)):
            if numbers[i]+numbers[k]+numbers[j]==target:
                print("The three digits that add up to",target,"are ",numbers[i],numbers[k],numbers[j],"indexed at")
                print([i,k,j])