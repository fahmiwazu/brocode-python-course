############### multi-level inheritance in python

class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("this animal is eating")

class Cat(Animal):
    def meow(self):
        print("this cat is meowing")

cat = Cat()
print(cat.alive)
cat.eat()
cat.meow()