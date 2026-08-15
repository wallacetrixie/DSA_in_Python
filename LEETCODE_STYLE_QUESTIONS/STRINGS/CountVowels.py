def CountVowels(name):
    vowels="aeiouAEIOU"
    count=0
    for char in name:
        if char in vowels:
            count+=1
    print("The string",name,"has",count,"vowels")
    return count
CountVowels("wAmbulwaombina")