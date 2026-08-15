def CountingWords(sentence):
    words=sentence.split()
    frequency={}
    for word in words:
        frequency[word]=frequency.get(word,0)+1
    return frequency
print(CountingWords("My name is wallace wambulwa and i love python"))