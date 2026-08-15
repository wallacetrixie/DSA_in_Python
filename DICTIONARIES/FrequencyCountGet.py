numbers=[1,1,2,3,4,4,3,2,5,5,6,7,6,7,9,7,7,9]
frequency={}
for number in numbers:
    frequency[number]=frequency.get(number,0)+1

print(frequency)