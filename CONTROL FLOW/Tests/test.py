"""Small control-flow test examples.

These examples avoid interactive input so they can be run directly as quick checks.
"""


def classify_access(age, balance):
	if age < 18:
		return "underage"
	elif balance < 1000:
		return "insufficient_balance"
	return "allowed"


def is_even(number):
	return number % 2 == 0


def prime_check(number):
	if number < 2:
		return False
	for divisor in range(2, number):
		if number % divisor == 0:
			return False
	return True


def count_until(limit):
	values = []
	counter = 0
	while counter < limit:
		values.append(counter)
		counter += 1
	return values


assert classify_access(16, 5000) == "underage"
assert classify_access(21, 500) == "insufficient_balance"
assert classify_access(21, 5000) == "allowed"

assert is_even(8) is True
assert is_even(7) is False

assert prime_check(2) is True
assert prime_check(9) is False

assert count_until(4) == [0, 1, 2, 3]

print("Control flow examples passed.")
