####################### How to pass object as argument in Python
class Car:
    color=None

class Motorcycle:
    color=None
def change_color(kendaraan,color):
    kendaraan.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
speda1= Motorcycle()
speda2= Motorcycle()
speda3= Motorcycle()

change_color(car_1,"black")
change_color(car_2,"white")
change_color(car_3,"blue")
change_color(speda1,"ireng")
change_color(speda2,"abang")
change_color(speda3,"abu")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(speda1.color)
print(speda2.color)
print(speda3.color)