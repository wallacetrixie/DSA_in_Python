number=453
hundreds= number //100 #1
units=(number //10) %10 #2
ones=number %10 #3

swapped= ones* 100 + units*10 + hundreds
print("The swapped number is:", swapped)
