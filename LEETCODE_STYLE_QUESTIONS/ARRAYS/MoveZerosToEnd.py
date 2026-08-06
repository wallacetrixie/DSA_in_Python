numbers=[12,76,0,2,65,22,0,56,0,23]
non_zeros=[]
zeros=[]
for i in range(len(numbers)):
    if numbers[i]==0:
        zeros.append(numbers[i])
    else:
        non_zeros.append(numbers[i])
print(non_zeros+zeros)