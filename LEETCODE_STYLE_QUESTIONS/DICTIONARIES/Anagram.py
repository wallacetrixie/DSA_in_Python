#Two strings are anagrams if they contain the same characters with the same frequencies.return true or false 
def Anagram(string1,string2):
    if len(string1)!=len(string2):
        return False
    frequency1={}
    frequency2={}
    for char in string1:
        frequency1[char]=frequency1.get(char,0)+1
        
    for char in string2:
        frequency2[char]=frequency2.get(char,0)+1

    return frequency1==frequency2

print(Anagram("wallace","wallace"))

