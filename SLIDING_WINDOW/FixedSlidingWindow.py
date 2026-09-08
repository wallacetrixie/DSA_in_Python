#Instead of repeatedly calculating information about every 
# possible subarray/substring, maintain a "window" and move it across the data.
#example given an array of strings, return the maximum sum of consecutive 3 digits

def SlidingWindow(numbers,k):
    windowSum=sum(numbers[:k])
    maxSum=windowSum

    for right in range(k,len(numbers)):
        windowSum +=numbers[right]
        windowSum-=numbers[right-k]

        maxSum=max(windowSum,maxSum)

    return maxSum
print(SlidingWindow([1,3,4,6,4,2,5,7,5],3))