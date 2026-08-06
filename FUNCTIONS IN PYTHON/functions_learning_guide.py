"""
Python Functions - Comprehensive Learning Guide
From basics to interview-ready patterns
"""

# ============================================================================
# PART 1: BASICS (Foundation)
# ============================================================================

print("=" * 60)
print("PART 1: BASICS")
print("=" * 60)

# 1. Simple function with no return
def greet():
    """Function with no parameters or return value."""
    print("Hello, Python learner!")

greet()


# 2. Function with parameters
def add(a, b):
    """Takes two numbers and returns their sum."""
    return a + b

result = add(5, 3)
print(f"add(5, 3) = {result}")


# 3. Multiple return values (interview favorite!)
def get_user_info():
    """Return multiple values as a tuple."""
    name = "Alice"
    age = 25
    city = "New York"
    return name, age, city  # Returns a tuple

name, age, city = get_user_info()  # Unpacking
print(f"User: {name}, Age: {age}, City: {city}")


# 4. Default parameters
def power(base, exponent=2):
    """Function with default parameter."""
    return base ** exponent

print(f"power(5) = {power(5)}")        # Uses default exponent=2
print(f"power(5, 3) = {power(5, 3)}")  # Overrides default


# ============================================================================
# PART 2: VARIADIC FUNCTIONS (*args, **kwargs) - Common in Interviews
# ============================================================================

print("\n" + "=" * 60)
print("PART 2: *args AND **kwargs")
print("=" * 60)

# Using *args (non-keyword arguments)
def sum_all(*args):
    """Accept any number of positional arguments."""
    print(f"Arguments received: {args}")
    total = sum(args)
    return total

print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")


# Using **kwargs (keyword arguments)
def print_config(**kwargs):
    """Accept any number of keyword arguments."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("Configuration:")
print_config(host="localhost", port=8080, debug=True, timeout=30)


# Combining both - IMPORTANT for interviews!
def flexible_function(required, *args, **kwargs):
    """Combine required params, *args, and **kwargs."""
    print(f"Required: {required}")
    print(f"Extra positional args: {args}")
    print(f"Keyword arguments: {kwargs}")

flexible_function("important", 1, 2, 3, name="test", level="debug")


# ============================================================================
# PART 3: LAMBDA FUNCTIONS - Short, Anonymous Functions
# ============================================================================

print("\n" + "=" * 60)
print("PART 3: LAMBDA FUNCTIONS")
print("=" * 60)

# Lambda for simple operations
square = lambda x: x ** 2
print(f"lambda x: x**2 applied to 5 = {square(5)}")

# Lambda with multiple parameters
multiply = lambda x, y: x * y
print(f"lambda x, y: x*y applied to (4, 7) = {multiply(4, 7)}")

# Lambda with map() - VERY COMMON in interviews
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")

# Lambda with filter() - VERY COMMON in interviews
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Lambda with sorted() - Common in interviews
words = ["python", "java", "go", "rust", "c"]
sorted_by_length = sorted(words, key=lambda word: len(word))
print(f"Words sorted by length: {sorted_by_length}")


# ============================================================================
# PART 4: HIGHER-ORDER FUNCTIONS - Functions that work with functions
# ============================================================================

print("\n" + "=" * 60)
print("PART 4: HIGHER-ORDER FUNCTIONS")
print("=" * 60)

# Function that takes another function as parameter
def apply_operation(a, b, operation):
    """Takes two numbers and a function to apply."""
    return operation(a, b)

result = apply_operation(10, 5, lambda x, y: x + y)
print(f"apply_operation(10, 5, add) = {result}")

result = apply_operation(10, 5, lambda x, y: x - y)
print(f"apply_operation(10, 5, subtract) = {result}")


# Function that returns another function (Closure)
def make_multiplier(factor):
    """Returns a function that multiplies by the given factor."""
    def multiplier(x):
        return x * factor
    return multiplier

times_three = make_multiplier(3)
times_five = make_multiplier(5)

print(f"times_three(10) = {times_three(10)}")
print(f"times_five(10) = {times_five(10)}")


# ============================================================================
# PART 5: RECURSION - Common Interview Problem!
# ============================================================================

print("\n" + "=" * 60)
print("PART 5: RECURSION")
print("=" * 60)

# Classic: Factorial
def factorial(n):
    """Calculate factorial recursively. Base case is crucial!"""
    if n <= 1:  # Base case - ESSENTIAL
        return 1
    return n * factorial(n - 1)  # Recursive case

print(f"factorial(5) = {factorial(5)}")


# Fibonacci sequence - Popular interview question
def fibonacci(n):
    """Return nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"fibonacci(6) = {fibonacci(6)}")  # 0, 1, 1, 2, 3, 5


# Sum of digits - Another common interview pattern
def sum_of_digits(n):
    """Sum all digits in a number recursively."""
    if n < 10:  # Base case
        return n
    return (n % 10) + sum_of_digits(n // 10)

print(f"sum_of_digits(12345) = {sum_of_digits(12345)}")


# ============================================================================
# PART 6: LIST COMPREHENSIONS - Pythonic way to process data
# ============================================================================

print("\n" + "=" * 60)
print("PART 6: LIST/DICT COMPREHENSIONS")
print("=" * 60)

# Basic list comprehension (alternative to map + lambda)
squares = [x ** 2 for x in range(1, 6)]
print(f"Squares: {squares}")

# List comprehension with condition (alternative to filter + lambda)
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# Dictionary comprehension
scores = {name: score for name, score in [("Alice", 90), ("Bob", 85), ("Charlie", 92)]}
print(f"Scores dict: {scores}")


# ============================================================================
# PART 7: COMMON INTERVIEW PATTERNS
# ============================================================================

print("\n" + "=" * 60)
print("PART 7: COMMON INTERVIEW PATTERNS")
print("=" * 60)

# Pattern 1: Count occurrences
def count_char(text, char):
    """Count how many times a character appears."""
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

print(f"Count of 'l' in 'hello': {count_char('hello', 'l')}")


# Pattern 2: Check if something is in a list
def contains_duplicate(numbers):
    """Check if list has duplicates - common interview question."""
    seen = set()
    for num in numbers:
        if num in seen:
            return True
        seen.add(num)
    return False

print(f"[1, 2, 3, 4] has duplicates: {contains_duplicate([1, 2, 3, 4])}")
print(f"[1, 2, 2, 4] has duplicates: {contains_duplicate([1, 2, 2, 4])}")


# Pattern 3: Reverse operations
def reverse_string(s):
    """Reverse a string - simple but common."""
    return s[::-1]

print(f"Reverse of 'hello': {reverse_string('hello')}")


# Pattern 4: Two-pointer technique
def is_palindrome(s):
    """Check if string is palindrome - interview classic."""
    s = s.lower()  # Handle case
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(f"Is 'racecar' palindrome: {is_palindrome('racecar')}")
print(f"Is 'hello' palindrome: {is_palindrome('hello')}")


# Pattern 5: Searching and finding max/min
def find_max(numbers):
    """Find maximum without using max() - shows logic."""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

print(f"Max of [5, 2, 8, 1, 9]: {find_max([5, 2, 8, 1, 9])}")


# ============================================================================
# PART 8: DECORATORS - Advanced but increasingly common in interviews
# ============================================================================

print("\n" + "=" * 60)
print("PART 8: DECORATORS (BONUS)")
print("=" * 60)

def my_decorator(func):
    """A simple decorator that wraps a function."""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Function completed")
        return result
    return wrapper

@my_decorator
def greet_user(name):
    """Greet a user."""
    return f"Hello, {name}!"

print(greet_user("Alice"))


# ============================================================================
# PART 9: REAL-WORLD APPLICATIONS
# ============================================================================

print("\n" + "=" * 60)
print("PART 9: REAL-WORLD APPLICATIONS")
print("=" * 60)

# Application 1: Data processing
def get_statistics(numbers):
    """Calculate multiple statistics at once."""
    if not numbers:
        return None
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)
    
    return {
        'sum': total,
        'average': average,
        'min': minimum,
        'max': maximum,
        'count': count
    }

data = [10, 20, 30, 40, 50]
stats = get_statistics(data)
print(f"Statistics: {stats}")


# Application 2: String manipulation
def is_valid_email(email):
    """Simple email validation - common in real projects."""
    if '@' not in email or '.' not in email:
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    return len(parts[0]) > 0 and len(parts[1]) > 0

print(f"Is 'user@example.com' valid: {is_valid_email('user@example.com')}")
print(f"Is 'invalid.email' valid: {is_valid_email('invalid.email')}")


# Application 3: Data transformation
def celsius_to_fahrenheit(celsius):
    """Convert temperature."""
    return (celsius * 9/5) + 32

temperatures_c = [0, 10, 20, 30, 40]
temperatures_f = [celsius_to_fahrenheit(t) for t in temperatures_c]
print(f"Celsius: {temperatures_c}")
print(f"Fahrenheit: {temperatures_f}")


print("\n" + "=" * 60)
print("END OF GUIDE")
print("=" * 60)
