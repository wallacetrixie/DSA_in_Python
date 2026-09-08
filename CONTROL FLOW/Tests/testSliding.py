def Sliding(marks,k):
    windowSum=sum(marks[:k])
    maxSum=windowSum

    for right in range(k,len(marks)):
        windowSum+=marks[right]
        windowSum-=marks[right-k]

        maxSum=max(windowSum,maxSum)

    return maxSum
print(Sliding([2,4,2,5,7,2,3,4],3))