# Control Flow Examples in Python

# 1. if-elif-else statement
age = int(input("Enter your age: "))
balance = int(input("Enter your current balance: "))
if age < 18:
    print("You are underage.")
elif balance < 1000:
    print("Insufficient balance to qualify.")
else:
    print("Welcome to the party!")

# 2. Nested if statement
score = int(input("Enter your test score: "))
if score >= 50:
    print("You passed.")
    if score >= 90:
        print("Excellent!")
else:
    print("You failed.")

# 3. while loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# 4. for loop with break and continue
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop at 7
    print(f"i = {i}")

# 5. pass statement
for letter in 'Python':
    if letter == 'h':
        pass  # Placeholder for future code
    print(f"Current letter: {letter}")

# 6. match-case statement (Python 3.10+)
command = input("Enter command (start/stop/exit): ")
match command:
    case "start":
        print("System starting...")
    case "stop":
        print("System stopping...")
    case "exit":
        print("Exiting program.")
    case _:
        print("Unknown command.")

# 7. Ternary operator
num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(f"The number is {result}.")