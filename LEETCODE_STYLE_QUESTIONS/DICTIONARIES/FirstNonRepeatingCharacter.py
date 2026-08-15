#First Non repeating character
def FirstNonRepeating(name):
    frequency={}
    for char in name:
        frequency[char]=frequency.get(char,0)+1
    for char in frequency:
        if frequency[char]==1:
            return char
    return None
print(FirstNonRepeating("wallacewambulwa"))

