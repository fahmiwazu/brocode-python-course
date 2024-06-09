############## Basic Class variable in python
from car import Car

car_1 = Car("Honda","Civic","2024","Black")
car_2 = Car("Jeep","Wrangler","2020","Camo")

car_2.wheels = 6    #   specific object
Car.wheels = 7      #   class object

print(car_1.wheels)
print(car_2.wheels)