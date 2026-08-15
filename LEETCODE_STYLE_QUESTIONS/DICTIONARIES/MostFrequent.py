#find the modal or the most frequent element
def Most_common(numbers):
    if len(numbers)<2:
        return False
    frequency={}
    
    for number in numbers:
        frequency[number]=frequency.get(number,0)+1
    common=numbers[0]

    for number in frequency:
        if frequency[number]>frequency[common]:
            common=number
    return common
print(Most_common([1,2,3,4,4,5,6,6,6,6,7,8,9,10]))