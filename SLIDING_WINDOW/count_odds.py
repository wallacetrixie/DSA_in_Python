def count_odds(numbers,k):
    odd_count=0
    for number in numbers[:k]:
        if number %2!=0:
            odd_count+=1
        result=[odd_count]

    for right in range(k,len(numbers)):
        if numbers[right] %2!=0:
            odd_count+=1

        if numbers[right-k] %2!=0:
            odd_count-=1

        result.append(odd_count)
    return result
print(count_odds([1,2,3,4,5,6,7,8,9],3))

