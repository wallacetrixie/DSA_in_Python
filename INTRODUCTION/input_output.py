Myname = input("Enter your name: ")
LuckyNumber = int(input("What is your Lucky number?: "))
print("Hello " + Myname + "! Your lucky number is " + str(LuckyNumber) + ".")

# Example 2: Taking two numbers and adding them
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print("The sum is:", sum_result)

# Example 3: Asking for a favorite color and responding
favorite_color = input("What is your favorite color?: ")
print("Wow!", favorite_color, "is a beautiful color!")

# Example 4: Checking if a number is even or odd
number = int(input("Enter a number to check if it's even or odd: "))
if number % 2 == 0:
	print(number, "is even.")
else:
	print(number, "is odd.")