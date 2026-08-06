def largest(number):
    maximum=number[0]
    for i in range(len(number)):
        if number[i]>maximum:
            maximum= number[i]
    return maximum
numbers=[76,33,21,44,9,99,36,63,55,97,63]
print("The largesst number is:",largest(numbers))