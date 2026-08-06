def SmallestNumber():
    numbers=[21,34,78,23,21,56,76,43,87,75,3,9,34,44,59,21]
    smallest=numbers[0]
    for i in range (len(numbers)):
        if numbers[i]< smallest:
            smallest=numbers[i]
            print("The smallest Number is:",smallest)
SmallestNumber()
