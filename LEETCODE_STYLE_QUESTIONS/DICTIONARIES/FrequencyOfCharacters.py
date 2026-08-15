#Given a string, count how many times each character appears.
name="wallacewambulwa"
frequency={}
for char in name:
    frequency[char]=frequency.get(char,0)+1
print(frequency)

for key,value in frequency.items():
    print(key,value)