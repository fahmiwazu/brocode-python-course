################ abstract Classes in python
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("Gassss")

    def stop(self):
        print("REMMM")


class Motorcycle(Vehicle):
    def go(self):
        print("Pancallllll")

    def stop(self):
        print("rem")

# kendaraan = Vehicle()
mobil = Car()
speda = Motorcycle()

mobil.go()
speda.go()

mobil.stop()
speda.stop()