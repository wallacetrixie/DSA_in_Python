#count numbers greater than X
def count_greater_x(numbers,k,x):
    count=0

    for number in numbers[:k]:
        if number>x:
            count+=1
        result=[count]
    for right in range(k,len(numbers)):
        if numbers[right]>x:
            count+=1
        if numbers[right-k]>x:
            count-=1
        result.append(count)
    return result
print(count_greater_x([1,2,3,4,5,6,7,8,9,10],3,2))
    
