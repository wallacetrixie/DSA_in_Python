def swapping():
    number=int(input("Enter a number:"))
    tens=number // 10
    units=number %10
    return units*10 +tens
print("The swapped number is:" , swapping())