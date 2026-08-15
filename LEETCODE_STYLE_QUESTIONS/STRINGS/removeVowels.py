def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""

    for ch in s:
        if ch not in vowels:
            result += ch

    return result