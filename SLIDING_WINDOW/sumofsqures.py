def sum_of_squares(numbers, k):
    window_sum = sum(number ** 2 for number in numbers[:k])
    result = [window_sum]

    for right in range(k, len(numbers)):
        window_sum += numbers[right] ** 2
        window_sum -= numbers[right - k] ** 2

        result.append(window_sum)

    return result


print(sum_of_squares([1, 2, 3, 4, 5], 3))