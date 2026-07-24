

def say_hello():
    print("Hello! Welcome to Python functions.")


def greet_user(name):
    print(f"Hello, {name}!")


def add_numbers(a, b):
    return a + b


def area_of_rectangle(length, width):
    return length * width


def show_basic_examples():
    say_hello()
    greet_user("Amina")
    print("2 + 3 =", add_numbers(2, 3))
    print("Area of 5 by 4 rectangle =", area_of_rectangle(5, 4))


if __name__ == "__main__":
    show_basic_examples()
