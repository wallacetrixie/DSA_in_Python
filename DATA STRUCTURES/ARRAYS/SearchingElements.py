#Searching for a specific element in an array using function
def Searching(marks, value):
    for i in range(len(marks)):
        if marks[i]==value:
            return i
    return -1

marks=[33,54,22,87,84,22,98,99,33,33]
print(Searching(marks,84))

    