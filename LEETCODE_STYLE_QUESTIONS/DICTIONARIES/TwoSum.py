#returns two values that add to a specific target
def Two_Sum(numbers,target):
    seen={}
    for number in numbers:
        complement=target-number
        if complement in seen:
          print(seen[complement],number)
          break
        seen[number]=number
Two_Sum([1,4,3,12,54,62,37,87],88)
        

