numbers=[1,1,2,2,3,4,5,5,6,7,4,4,1,2]
frequency={}
for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
print(frequency)