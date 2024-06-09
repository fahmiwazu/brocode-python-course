################## method over writing in python
class Animal:
    def eat(self):
        print("this animal is eating")

class Rabbit:
    def eat(self):
        print("this rabbit is eating carrot")

klinci= Animal()
klinci.eat()
klinci = Rabbit()
klinci.eat()