def average_window(numbers,k):
    window_sum=sum(numbers[:k])
    averages=[window_sum/k]

    for right in range(k,len(numbers)):
        window_sum+=numbers[right]
        window_sum-=numbers[right-k]

        averages.append(window_sum/k)

    return averages
print(average_window([1,2,3,4,5,6,7,8,9],3))