def LargestNumber():
    numbers=[21,34,78,23,21,56,76,43,87,75,3,9,34,44,59,21]
    maximum=numbers[0]
    for i in range (len(numbers)):
        if numbers[i]>maximum:
            maximum=numbers[i]
    print("The largest number is:",maximum)

LargestNumber()


