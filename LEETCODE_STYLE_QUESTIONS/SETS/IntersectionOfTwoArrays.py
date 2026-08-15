#Given two arrays, return their common elements.
def CommonElements(mark1,mark2):
    set1=set(mark1)
    set2=set(mark2)
    return set1 &set2
print(CommonElements([12,23,43,54,32,34],[12,34,56,23,65,44]))


