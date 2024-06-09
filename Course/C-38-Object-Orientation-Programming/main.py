################# Object Orientation Programming in python
from car import Car

car_1 = Car("Honda","Civic","2024","Black")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()
car_1.stop()

car_2 = Car("Jeep","Wrangler","2020","Camo")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()
car_2.stop()