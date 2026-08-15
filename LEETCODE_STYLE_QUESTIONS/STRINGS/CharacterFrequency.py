def frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    print(freq)
    return freq
frequency("wallace")