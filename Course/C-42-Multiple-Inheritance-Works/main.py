######### multiple inheritance works in python

class Prey:
    def flee(self):
        print("ngibrittt")

class Predator:
    def hunt(self):
        print("pantawww")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

klinci = Rabbit()
e_lang = Hawk()
iwak = Fish()

klinci.flee()
e_lang.hunt()
iwak.hunt()
iwak.flee()
