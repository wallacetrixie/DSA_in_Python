# Python Functions - Interview Guide & Key Concepts

## 📚 Learning Path Overview

### Level 1: Basics (Fundamentals)
- Simple functions
- Functions with parameters & return values
- Default parameters

**Why it matters in interviews:** Interviewers expect you to understand function basics deeply. You should be able to explain *why* you use functions (code reusability, readability).

---

## 🎯 Key Concepts Explained

### 1. **Return Values**
```python
def multiply(a, b):
    return a * b

result = multiply(5, 8)  # result = 40
```
**Interview Tip:** Always understand the difference between a function that prints vs. returns a value. Printing is only for display; returning allows you to use the value in further calculations.

---

### 2. **Multiple Return Values** ⭐ (Very Common in Interviews)
```python
def get_name_and_age():
    return "Alice", 25  # Returns a tuple

name, age = get_name_and_age()  # Unpacking
```
**Interview Tip:** Interviewers often ask you to write functions that calculate multiple things. Returning multiple values is Pythonic and efficient.

---

### 3. ***args* (Variable Positional Arguments)**
```python
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4, 5)  # Works with any number of arguments
```
**Interview Tip:** `*args` allows flexibility. Common in interview questions where the input size varies. Remember: `args` becomes a **tuple**.

---

### 4. ****kwargs* (Variable Keyword Arguments)**
```python
def print_config(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_config(host="localhost", port=8080, debug=True)
```
**Interview Tip:** Use `**kwargs` when you need named parameters. Great for configuration functions or API calls.

---

### 5. **Lambda Functions** ⭐ (Frequently Tested)
```python
# Lambda is a quick, anonymous function
square = lambda x: x ** 2

# Often used with map, filter, sorted
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```
**Interview Tip:** Lambda + map/filter is VERY common in technical interviews. Practice this combination!

---

### 6. **Map, Filter, Sorted with Lambda** ⭐⭐ (Most Common)

#### Map: Transform each element
```python
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))  # [2, 4, 6, 8]
```

#### Filter: Keep only elements that satisfy condition
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4, 6]
```

#### Sorted: Sort with custom key
```python
words = ["python", "java", "go"]
by_length = sorted(words, key=lambda w: len(w))  # ["go", "java", "python"]
```

**Interview Tip:** These three are tested constantly. If you see a "transform", "filter", or "sort" problem, lambda + map/filter/sorted is often the solution.

---

### 7. **Higher-Order Functions** (Functions working with functions)
```python
def apply_operation(a, b, operation):
    return operation(a, b)

result = apply_operation(10, 5, lambda x, y: x + y)  # 15
```
**Interview Tip:** Shows understanding of functions as first-class objects. Common in functional programming questions.

---

### 8. **Closures** (Functions returning functions)
```python
def make_adder(n):
    def adder(x):
        return x + n  # n is "captured" from outer scope
    return adder

add_5 = make_adder(5)
print(add_5(10))  # 15
```
**Interview Tip:** Demonstrates understanding of scope and function factories. Advanced but increasingly common.

---

### 9. **Recursion** ⭐⭐ (Critical for Interviews)

#### Key Rule: Every recursive function needs a **BASE CASE**
```python
def factorial(n):
    if n <= 1:  # ⬅️ BASE CASE (stops recursion)
        return 1
    return n * factorial(n - 1)  # Recursive case
```

**Common Recursive Problems:**
- **Factorial:** n! = n × (n-1)!
- **Fibonacci:** fib(n) = fib(n-1) + fib(n-2)
- **Sum of digits:** Extract last digit, add to sum of remaining digits
- **Tree traversal:** Process nodes recursively
- **Backtracking:** Try option, recurse, undo if needed

**Interview Tip:** Recursion is tested heavily. Practice identifying when to use it and always have a clear base case.

---

### 10. **List Comprehensions** ⭐ (Pythonic & Efficient)
```python
# Instead of:
squares = []
for x in range(5):
    squares.append(x ** 2)

# Write this (cleaner):
squares = [x ** 2 for x in range(5)]

# With condition:
evens = [x for x in range(10) if x % 2 == 0]

# Nested:
matrix = [[i*j for j in range(3)] for i in range(3)]
```
**Interview Tip:** Interviewers prefer list comprehensions over loops. Shows Pythonic thinking. Can often replace map/filter.

---

## 🔥 Common Interview Patterns

### Pattern 1: Two-Pointer Technique
```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```
**Used for:** String/array problems, checking palindromes, reversing

---

### Pattern 2: Hash Map for Counting
```python
def count_elements(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts
```
**Used for:** Frequency counting, finding duplicates, anagrams

---

### Pattern 3: Two-Sum Pattern
```python
def find_two_sum(numbers, target):
    seen = set()
    for num in numbers:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None
```
**Used for:** Finding pairs, complement problems

---

### Pattern 4: Check Duplicates
```python
def has_duplicates(numbers):
    return len(numbers) != len(set(numbers))
```
**Used for:** Validation, constraint checking

---

## 🎓 Interview Preparation Strategy

### Must Know:
1. ✅ Basic function definition and return values
2. ✅ Default parameters
3. ✅ *args and **kwargs
4. ✅ Lambda functions
5. ✅ map(), filter(), sorted()
6. ✅ List comprehensions
7. ✅ Basic recursion
8. ✅ Simple algorithm patterns (two-pointer, hash map)

### Nice to Know:
1. Decorators
2. Higher-order functions
3. Closures
4. Advanced recursion (memoization)

### Common Interview Questions:

**Q1: Write a function that reverses a list**
```python
def reverse_list(lst):
    return lst[::-1]  # Or use two-pointer
```

**Q2: Write a function to find the second largest number**
```python
def second_largest(numbers):
    unique = list(set(numbers))
    return sorted(unique)[-2]
```

**Q3: Write a function to check if strings are anagrams**
```python
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
```

**Q4: Write a function to flatten a nested list**
```python
def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))  # Recursion!
        else:
            result.append(item)
    return result
```

---

## 💡 Pro Tips for Interviews

1. **Start Simple:** Always explain your approach before coding
2. **Think Out Loud:** Interviewers want to see your thought process
3. **Test Your Code:** Walk through an example before submitting
4. **Handle Edge Cases:** Empty lists, None values, negative numbers
5. **Optimize:** First get it working, then optimize if asked
6. **Know Complexity:** Understand O(n) vs O(n²) for your solution

---

## 📊 Quick Reference

| Concept | When to Use | Interview Frequency |
|---------|-----------|-------------------|
| Basic functions | Always | ⭐⭐⭐⭐⭐ |
| Return values | Always | ⭐⭐⭐⭐⭐ |
| Default params | Optional parameters | ⭐⭐⭐ |
| *args/**kwargs | Flexible functions | ⭐⭐⭐ |
| Lambda | Quick, small functions | ⭐⭐⭐⭐ |
| map/filter | Transforming data | ⭐⭐⭐⭐ |
| Recursion | Tree/divide-and-conquer | ⭐⭐⭐⭐⭐ |
| List comprehension | Transforming lists | ⭐⭐⭐⭐ |
| Closures | Advanced patterns | ⭐⭐ |

---

## 🚀 Next Steps

1. Run the `functions_learning_guide.py` file
2. Modify examples to understand deeply
3. Practice writing functions for these patterns
4. Solve LeetCode "Easy" problems using functions
5. Write your own functions for real problems
