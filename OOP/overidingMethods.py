class Animals:
    def Sound(self):
        print("Animals produce different sounds")
class Cat(Animals):
    def Sound(self):
        print("A cat meows")
class Dog(Animals):
    def Sound(self):
           print("A dog Barks")

cat1=Cat()
dog1=Dog()

cat1.Sound()
dog1.Sound()