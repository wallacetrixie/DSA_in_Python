#You are given n distinct numbers from the range:0 → n One number is missing. Find it.
def MissingNumber(numbers):
    missing=set(numbers)
    for i in range(len(numbers)+1):
        if i not in missing:
            return i
print(MissingNumber([0,2,3,4,5]))

