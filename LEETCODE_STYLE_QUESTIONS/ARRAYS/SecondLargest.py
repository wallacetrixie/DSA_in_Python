def Second_Largest(number):
    if len(number)< 2:
        return None
    largest=float('-inf')
    second=float('-inf')
    for i in range(len(number)):
        if number[i]>largest:
            second=largest
            largest=number[i]
        elif largest >number[i] > second:
            second=number[i]
    if second ==float('-inf'):
        return None
    return second
number=[23,65,5,23,89,65,88,60,0,100,34,22,46,79,99]
print("The second largest number is:",Second_Largest(number))
