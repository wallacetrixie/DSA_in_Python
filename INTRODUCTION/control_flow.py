#Loops and control statements/ if else loops
Age=int(input("Enter your age:"))
Balance=int(input("Enter your current balance:"))
if Age<18 or Balance <1000:
    print("Sorry you dont qualify for the party:")

else:
    print("Welcome in")


#For loops
for i in range(10):
    print(i)