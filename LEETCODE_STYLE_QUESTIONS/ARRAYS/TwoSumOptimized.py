numbers=[21,34,78,23,21,56,76,43,87,75,3,9,34,44,59,21,83,76,37,87,37]
target=12
seen={}
for i in range(len(numbers)):
    value=numbers[i]
    remainder=target-value
    if remainder in seen:
        print([seen[remainder],i])
        break
    seen[i]=i