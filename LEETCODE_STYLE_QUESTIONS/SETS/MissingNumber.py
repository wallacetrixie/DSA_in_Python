#You are given n distinct numbers from the range:0 → n One number is missing. Find it.
numbers=[1,2,3,4,5,7,8]
full=[]
largest=max(numbers) #5
smallest=min(numbers) #1
for i in range(smallest,largest+1):
    full.append(i)
print(full)
A=set(numbers)
B=set(full)
print("The missing number is:",B-A)
