#example reverse an array or a list using two pointers
def ReverseArray(marks):
    left=0
    right=len(marks)-1
    while left<right:
        marks[left],marks[right]=marks[right],marks[left]
        left+=1
        right-=1
    return marks
print(ReverseArray([12,23,6,2,12,56,87,43,66]))
#time and space complexity is O(n) and space =O(1)