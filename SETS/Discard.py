#unlike the remove method, discard does not show error when a value does not exist
numbers={1,2,3,4,5,6,7,8,9,10}
numbers.discard(11)
print(numbers)