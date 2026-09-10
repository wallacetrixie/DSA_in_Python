#returns the minimus sum of k consecutive size digits in a window
def MinimumSum(numbers,k):
    windowsSum=sum(numbers[:k])
    minimumSum=windowsSum

    for right in range(k,len(numbers)):
        windowsSum+=numbers[right]
        windowsSum-=numbers[right-k]

        minimumSum=min(windowsSum,minimumSum)
    return minimumSum

print(MinimumSum([1,2,3,4,5,6,7,8,9],3))