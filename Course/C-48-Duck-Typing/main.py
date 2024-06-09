############### Duck Typing in Python
class Duck:
    def walk(self):
        print("wek wek mlaku")

    def talk(self):
        print("wek wek wek wek")

class Chicken:
    def walk(self):
        print("ptok ptok mlaku")

    def talk(self):
        print("ptok ptok ptok ptok")

class Person():
    def catch(self, Wekk):
        Wekk.walk()
        Wekk.talk()
        print("entuk wek wek wek")

wek = Duck()
ptok = Chicken()
wong = Person()

wong.catch(wek)
wong.catch(ptok)