
def Palindrome(name):
    reversed=name[::-1]
    if reversed==name:
        print("The string is palindrome")
    else:
        print("The string is not palindrome")
    return reversed
Palindrome("wambulwa")
#alternative method without slicing
def palindrome(value):
    reverse=""
    for char in value:
        reverse=char+reverse
    if reverse==value:
        print("The string is palindrome")
    else:
        print("The string is not palindrome")
    return reverse
palindrome("omo")

