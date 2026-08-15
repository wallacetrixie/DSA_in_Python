#Coding Problem #2 — Find Duplicate numbers
def Dupplicate(numbers):
    frequency={}
    for number in numbers:
        frequency[number]=frequency.get(number,0)+1
    dupplicates=[]
    for number,count in frequency.items():
        if count>1:
            dupplicates.append(number)

    return dupplicates
print(Dupplicate([1,1,2,2,3,3,3,4,5,6,6,7,5,7,8,8,9,9,10]))

#returns numbers that have dupplicates