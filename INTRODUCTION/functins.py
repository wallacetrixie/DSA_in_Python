"""
functins.py
Comprehensive examples of function types in Python.
"""

def simple_function():
    """A simple function with no parameters and no return value."""
    print("This is a simple function.")

def function_with_parameters(a, b):
    """A function with parameters."""
    print(f"Sum of {a} and {b} is {a + b}")

def function_with_return(a, b):
    """A function that returns a value."""
    return a * b

def function_with_default_param(name="World"):
    """A function with a default parameter."""
    print(f"Hello, {name}!")

def function_with_variable_args(*args):
    """A function that accepts any number of positional arguments."""
    print("Arguments:", args)

def function_with_keyword_args(**kwargs):
    """A function that accepts any number of keyword arguments."""
    print("Keyword arguments:", kwargs)

def function_with_both_args(*args, **kwargs):
    """A function that accepts both positional and keyword arguments."""
    print("Args:", args)
    print("Kwargs:", kwargs)

def recursive_function(n):
    """A recursive function example (factorial)."""
    if n == 0:
        return 1
    else:
        return n * recursive_function(n - 1)

def lambda_function_example():
    """An example of a lambda (anonymous) function."""
    square = lambda x: x * x
    print("Square of 5:", square(5))

def function_with_docstring():
    """This function demonstrates a docstring for documentation."""
    pass

# Example usages (uncomment to test):
# simple_function()
# function_with_parameters(3, 4)
# print(function_with_return(3, 5))
# function_with_default_param()
# function_with_default_param("Alice")
# function_with_variable_args(1, 2, 3)
# function_with_keyword_args(a=1, b=2)
# function_with_both_args(1, 2, x=10, y=20)
# print(recursive_function(5))
# lambda_function_example()
def multiplication(a,b):
    return a * b
result=multiplication(5,8)
print("The multiplication of 5 and 8 is:", result)