def Dupplicate(numbers):
    dupplicates=set(numbers)
    return len(numbers)!=len(dupplicates)
print(Dupplicate([1,2,3,4,5,3,2,9,6,7,8,9]))