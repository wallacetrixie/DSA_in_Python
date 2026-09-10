#the trick is number>0
def count_positives(numbers, k):
    positive_count = 0

    for number in numbers[:k]:
        if number > 0:
            positive_count += 1

    result = [positive_count]

    for right in range(k, len(numbers)):

        if numbers[right] > 0:
            positive_count += 1

        if numbers[right - k] > 0:
            positive_count -= 1

        result.append(positive_count)

    return result


print(count_positives([-2, 4, 5, -1, 7], 3))