def window_products(numbers, k):
    product = 1
    zero_count = 0

    for number in numbers[:k]:
        if number == 0:
            zero_count += 1
        else:
            product *= number

    result = [0 if zero_count > 0 else product]

    for right in range(k, len(numbers)):

        # Add incoming
        incoming = numbers[right]

        if incoming == 0:
            zero_count += 1
        else:
            product *= incoming

        # Remove outgoing
        outgoing = numbers[right - k]

        if outgoing == 0:
            zero_count -= 1
        else:
            product //= outgoing

        result.append(0 if zero_count > 0 else product)

    return result