"""
Python Functions - Practice Problems
Try solving these before checking the solutions!
"""

# ============================================================================
# EASY LEVEL (Build Confidence)
# ============================================================================

print("=" * 70)
print("EASY LEVEL PROBLEMS")
print("=" * 70)

# EASY 1: Simple calculation
print("\n[EASY 1] Write a function that calculates the area of a rectangle")
print("Given: length=5, width=3")
print("Expected: 15")

def area_of_rectangle(length, width):
    """Calculate area of rectangle."""
    return length * width

print(f"Solution: {area_of_rectangle(5, 3)}\n")


# EASY 2: String manipulation
print("[EASY 2] Write a function that returns initials from a name")
print("Given: 'John Doe'")
print("Expected: 'JD'")

def get_initials(name):
    """Get initials from a name."""
    words = name.split()
    return ''.join([word[0].upper() for word in words])

print(f"Solution: {get_initials('John Doe')}\n")


# EASY 3: List operation
print("[EASY 3] Write a function that returns the average of a list")
print("Given: [10, 20, 30, 40]")
print("Expected: 25")

def average(numbers):
    """Calculate average of numbers."""
    return sum(numbers) / len(numbers)

print(f"Solution: {average([10, 20, 30, 40])}\n")


# EASY 4: Boolean check
print("[EASY 4] Write a function that checks if a number is even")
print("Given: 4")
print("Expected: True")

def is_even(n):
    """Check if number is even."""
    return n % 2 == 0

print(f"Solution: {is_even(4)} and {is_even(5)}\n")


# EASY 5: String reversal
print("[EASY 5] Write a function that reverses a string")
print("Given: 'python'")
print("Expected: 'nohtyp'")

def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

print(f"Solution: {reverse_string('python')}\n")


# ============================================================================
# MEDIUM LEVEL (Build Logic)
# ============================================================================

print("=" * 70)
print("MEDIUM LEVEL PROBLEMS")
print("=" * 70)

# MEDIUM 1: List processing with condition
print("\n[MEDIUM 1] Filter numbers greater than 10 from a list")
print("Given: [5, 15, 8, 20, 3, 12]")
print("Expected: [15, 20, 12]")

def filter_greater_than(numbers, threshold):
    """Filter numbers greater than threshold."""
    return [n for n in numbers if n > threshold]

result = filter_greater_than([5, 15, 8, 20, 3, 12], 10)
print(f"Solution: {result}\n")


# MEDIUM 2: Check if palindrome
print("[MEDIUM 2] Check if a string is a palindrome")
print("Given: 'racecar'")
print("Expected: True")

def is_palindrome(s):
    """Check if string is palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(f"Solution: {is_palindrome('racecar')} and {is_palindrome('hello')}\n")


# MEDIUM 3: Count occurrences
print("[MEDIUM 3] Count how many times each character appears")
print("Given: 'hello'")
print("Expected: {'h': 1, 'e': 1, 'l': 2, 'o': 1}")

def count_characters(s):
    """Count character occurrences."""
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    return counts

print(f"Solution: {count_characters('hello')}\n")


# MEDIUM 4: Find max without using max()
print("[MEDIUM 4] Find the maximum number without using max()")
print("Given: [3, 9, 2, 8, 1]")
print("Expected: 9")

def find_max(numbers):
    """Find maximum number."""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

print(f"Solution: {find_max([3, 9, 2, 8, 1])}\n")


# MEDIUM 5: Simple duplicate check
print("[MEDIUM 5] Check if list contains duplicates")
print("Given: [1, 2, 3, 2, 4]")
print("Expected: True")

def has_duplicates(lst):
    """Check if list has duplicates."""
    return len(lst) != len(set(lst))

print(f"Solution: {has_duplicates([1, 2, 3, 2, 4])} and {has_duplicates([1, 2, 3, 4])}\n")


# MEDIUM 6: Two-sum problem (find two numbers that add to target)
print("[MEDIUM 6] Find two numbers that add up to target")
print("Given: numbers=[2, 7, 11, 15], target=9")
print("Expected: (2, 7)")

def two_sum(numbers, target):
    """Find two numbers that sum to target."""
    seen = set()
    for num in numbers:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None

print(f"Solution: {two_sum([2, 7, 11, 15], 9)}\n")


# ============================================================================
# INTERMEDIATE LEVEL (Challenge Yourself)
# ============================================================================

print("=" * 70)
print("INTERMEDIATE LEVEL PROBLEMS")
print("=" * 70)

# INTERMEDIATE 1: Factorial with recursion
print("\n[INTERMEDIATE 1] Calculate factorial recursively")
print("Given: 5")
print("Expected: 120 (5! = 5×4×3×2×1)")

def factorial(n):
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"Solution: {factorial(5)}\n")


# INTERMEDIATE 2: Fibonacci sequence
print("[INTERMEDIATE 2] Get the nth Fibonacci number")
print("Given: 6")
print("Expected: 8 (sequence: 0, 1, 1, 2, 3, 5, 8...)")

def fibonacci(n):
    """Get nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Solution: {fibonacci(6)}\n")


# INTERMEDIATE 3: Anagram check
print("[INTERMEDIATE 3] Check if two strings are anagrams")
print("Given: 'listen' and 'silent'")
print("Expected: True")

def are_anagrams(s1, s2):
    """Check if strings are anagrams."""
    return sorted(s1.lower()) == sorted(s2.lower())

print(f"Solution: {are_anagrams('listen', 'silent')} and {are_anagrams('hello', 'world')}\n")


# INTERMEDIATE 4: Flatten nested list
print("[INTERMEDIATE 4] Flatten a nested list")
print("Given: [[1, 2], [3, [4, 5]], 6]")
print("Expected: [1, 2, 3, 4, 5, 6]")

def flatten(nested):
    """Flatten nested list using recursion."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(f"Solution: {flatten([[1, 2], [3, [4, 5]], 6])}\n")


# INTERMEDIATE 5: Process data and return multiple values
print("[INTERMEDIATE 5] Analyze a list and return multiple statistics")
print("Given: [1, 2, 3, 4, 5]")
print("Expected: (sum, average, min, max)")

def analyze_list(numbers):
    """Return multiple statistics."""
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg, min(numbers), max(numbers)

total, avg, minimum, maximum = analyze_list([1, 2, 3, 4, 5])
print(f"Solution: sum={total}, average={avg}, min={minimum}, max={maximum}\n")


# INTERMEDIATE 6: Filter and transform with map/lambda
print("[INTERMEDIATE 6] Square all even numbers in a list")
print("Given: [1, 2, 3, 4, 5, 6]")
print("Expected: [4, 16, 36] (only evens, squared)")

def square_evens(numbers):
    """Square only even numbers."""
    evens = [n for n in numbers if n % 2 == 0]
    return [n ** 2 for n in evens]

print(f"Solution: {square_evens([1, 2, 3, 4, 5, 6])}\n")


# INTERMEDIATE 7: Using *args
print("[INTERMEDIATE 7] Create a function that returns sum and product of any numbers")
print("Given: 2, 3, 4")
print("Expected: (sum=9, product=24)")

def sum_and_product(*args):
    """Return sum and product of any numbers."""
    total_sum = sum(args)
    product = 1
    for n in args:
        product *= n
    return total_sum, product

result = sum_and_product(2, 3, 4)
print(f"Solution: sum={result[0]}, product={result[1]}\n")


# INTERMEDIATE 8: Using **kwargs for configuration
print("[INTERMEDIATE 8] Create a printer function that takes any configuration")
print("Given: print_box(text='Hello', width=10, char='*')")
print("Expected: A box around the text")

def print_box(**kwargs):
    """Print text in a box with configuration."""
    text = kwargs.get('text', 'Hello')
    width = kwargs.get('width', 10)
    char = kwargs.get('char', '*')
    
    print(char * width)
    print(f"{text.center(width)}")
    print(char * width)

print("Solution:")
print_box(text='Hello', width=15, char='*')


# ============================================================================
# CHALLENGE PROBLEMS (Advanced)
# ============================================================================

print("\n" + "=" * 70)
print("CHALLENGE PROBLEMS (Try these last!)")
print("=" * 70)

# CHALLENGE 1: Recursive string reversal
print("\n[CHALLENGE 1] Reverse a string using recursion (no slicing)")
print("Given: 'python'")
print("Expected: 'nohtyp'")

def reverse_recursive(s):
    """Reverse string recursively."""
    if len(s) == 0:
        return s
    return s[-1] + reverse_recursive(s[:-1])

print(f"Solution: {reverse_recursive('python')}\n")


# CHALLENGE 2: Find longest word
print("[CHALLENGE 2] Find the longest word in a list")
print("Given: ['python', 'java', 'javascript', 'go']")
print("Expected: 'javascript'")

def longest_word(words):
    """Find longest word."""
    return max(words, key=len)

print(f"Solution: {longest_word(['python', 'java', 'javascript', 'go'])}\n")


# CHALLENGE 3: Partition list by condition
print("[CHALLENGE 3] Partition list into two: numbers <= 5 and > 5")
print("Given: [1, 6, 3, 9, 2, 8]")
print("Expected: ([1, 3, 2], [6, 9, 8])")

def partition(numbers, threshold):
    """Partition list by threshold."""
    less_equal = [n for n in numbers if n <= threshold]
    greater = [n for n in numbers if n > threshold]
    return less_equal, greater

result = partition([1, 6, 3, 9, 2, 8], 5)
print(f"Solution: {result}\n")


# CHALLENGE 4: Remove duplicates while preserving order
print("[CHALLENGE 4] Remove duplicates from list (keep order)")
print("Given: [1, 2, 2, 3, 1, 4, 2]")
print("Expected: [1, 2, 3, 4]")

def remove_duplicates(lst):
    """Remove duplicates preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(f"Solution: {remove_duplicates([1, 2, 2, 3, 1, 4, 2])}\n")


print("=" * 70)
print("PRACTICE COMPLETE! 🎉")
print("=" * 70)
print("\nNext steps:")
print("1. Try solving each problem without looking at solutions")
print("2. Test your solutions with different inputs")
print("3. Modify solutions to handle edge cases")
print("4. Practice on LeetCode Easy problems")
