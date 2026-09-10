def count_even(numbers,k):
    even_count=0

    for number in numbers[:k]:
        if number %2==0:
            even_count+=1
    result=[even_count]
    
    for right in range(k,len(numbers)):
        if numbers[right]%2==0:
            even_count+=1

        if numbers[right-k]%2==0:
            even_count-=1

        result.append(even_count)
    return result
print(count_even([1,2,2,4,2,6,7,8,9,10],3))

    
