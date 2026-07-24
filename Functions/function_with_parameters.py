


def calculate_average(math_score, science_score, english_score):
    total = math_score + science_score + english_score
    return total / 3


def is_even(number):
    return number % 2 == 0


def create_full_name(first_name, last_name):
    return f"{first_name} {last_name}"


def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def show_parameter_examples():
    average = calculate_average(80, 75, 90)
    print("Average score:", average)
    print("Is 14 even?", is_even(14))
    print("Full name:", create_full_name("John", "Doe"))
    print("25°C in Fahrenheit:", convert_celsius_to_fahrenheit(25))


if __name__ == "__main__":
    show_parameter_examples()
