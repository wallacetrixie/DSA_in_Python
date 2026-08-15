squares={}
for i in range(1,11):
    if i%2==0:
         squares[i]=i*i   
for key,value in squares.items():
    print(key,value)