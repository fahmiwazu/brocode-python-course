# print("hello worlde")
# print("its really good")
###########Getting Starterddddd
# first_name = "Waz"
# lasT_name = "zouu"
# full_name = first_name + lasT_name
# print(type(full_name))
# print("hello " + full_name)
########## Variable
# age = 24
# age += 1
# print(age)
# print(type(age))
# print("Your age is "+ str(age))
#
# height = 168.88
# print("your height is " + str(height) + "cm")
# print(type(height))
#
# human = True
# print("are you a human : " + str(human))
# print(type(human))
######### Multiple Assignment
# name = ("waz")
# age = 27
# attractive = True
# name, age, attractive = "waz", 25, True

# print(name)
# print(age)
# print(attractive)

# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

# Spongebob = Patrick = Sandy = Squidward = 30

# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)

############## String Method
# name = "wazo uuu"
#
# print(len(name))
# print(name.find("a"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("u"))
# print(name.replace("o","a"))
# print(name*3)

############# Type Casting
#
# x = 1       #int
# y = 2.0     #flt
# z = "3"   #str
#
# print(x)
# print(y)
# print(z)
#
# print(int(y))
# print(z*3)
#
# x = float(x)
# y = int(y)
# z = int(z)
#
# print(x)
# print(y)
# print(z*3)

####### Console
#
# name = input("What is your name ? : ")
# age = int(input("How old are you ? : "))
# height = float(input("How tall are you ? : "))
#
# age += 1
# print("hello "+ name)
# print("you are  "+ str(age) + " years old")
# print("You are "+ str(height) + " cm tall")

######### MATTHHEEE
# import math
# pi = 3.14
# x=1
# y=2
# z=3
#
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(16))
# print(max(x,y,z))
# print(min(x,y,z))

######### String Slicing
# name = "Fahmi Wazu"
# first_name = name[:6]
# last_name = name[6:]
# funky_name = name[::2]
# reversed_name  = name[::-1]
#
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
#
# slice = slice(7,-4)
# print(website1[slice])
# print(website2[slice])

############### If Statement
# age = int(input("How old are you? : "))
#
# if age == 100:
#     print("you are sepuh")
# elif age >= 18:
#     print("you are an adult")
# elif age < 0:
#     print("you havent born yet")
# else:
#     print("You are a child")

############## Logical Operator
# temp = int(input("What's the temperature outside? : "))
#
# if not (temp <= 0 and temp >= 30) :
#     print("wokayyy")
# elif not (temp > 0 or temp < 30):
#     print("nayyy")

############ While loop
# while 1==1:
#     print("help im stuck in a loop")

# name = ""
#while len(name)==0:

# name = None
# while not name:
#     name = input("Enter your name ? : ")
#
# print("Hello "+ name)

################ For loop
# import time
# for i in range(10):
#     print(i+1)

# for i in range(50,100+1,2):
#     print(i)

# for i in "Fahmi Wazu":
#     print(i)

# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!!")

########### Nested Loop
# rows = int(input("How many rows ? : "))
# columns = int(input("How many columns ? : "))
# symbol = input("Enter symbol to use : ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

########## Loop Control Statement
# while True:
#     name = input("Enter your name? : ")
#     if name != "":
#         break

# phone_number = "123-456-789-0"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i,end="")

# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)

############# List
# food = ["rendang","kebab","nasgor","borgar","podeng"]
# print(food)
# food[0]="Sambal"
# food.append("Ice Cream")
# food.remove("borgar")
# food.pop()
# food.insert(0,"cake")
# food.sort()
# food.clear()

# for i in food:
#     print(i)

############# 2D List
# drink = ["kopi","soda","teh"]
# dinner = ["mie","nasgor","soto"]
# snack = ["astor","kentunk"]
#
# food = [drink,dinner,snack]
#
# print(food)
# print(food[0][2])
# print(food[1][0])
# print(food[2][1])

############ Tuple
# student = ("Waz",24,"Lanang")
# print(student.count("Waz"))
# print(student.index("Lanang"))
#
# for x in student:
#     print(x)
#
# if "Waz" in student:
#     print("Waz is here")

########## Set
# dapur = {"fork","spoon","knife"}
# piring = {"mangkok","piring","gelas","knife"}
# dapur.add("gombal")
# dapur.remove("spoon")
# dapur.clear()
# dapur.update(piring)
# dinner_table = dapur.union(piring)
# for i in dinner_table:
#     print(i)
# print(piring.difference(dapur))
# print(dapur.intersection(piring))

########### Dictionary
# capitals = {'USA':'DC',
#             'Indo':'Jkt',
#             'Jpn':'Tokyo',
#             'Russia':'Moscow'}
#
# capitals.update({'Jerman':'Berlin'})
# capitals.update({'Indo':'IKN'})
# capitals.pop('Jpn')
# capitals.clear()

# print(capitals['Indo'])
# print(capitals['German'])
# print(capitals.get('German'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key,value in capitals.items():
#     print(key, value)

############## Index Operator[]
# name = "fahmi Wazu!"
#
# if(name[0].islower()):
#     name = name.capitalize()
#
# first_name = name[:5].upper()
# last_name = name[6:].lower()
# last_character = name[-1]
#
# print(name)
# print(first_name)
# print(last_name)
# print(last_character)

############# Function
# def Hello(first_name, last_name, age):
#     print("hello! "+first_name+" "+last_name)
#     print("you are "+ str(age) + " years old")
#     print("have a nice day")
#
# Hello("Fahmi","Wazu",21)

############# return statement
# def multiply(number1,number2):
#     return number1 * number2
#
# x=multiply(6,8)
# print(x)

########## Keyword argument
# def hello(first,middle,last):
#     print("hello "+first+" "+middle+" "+last)
#
# hello(last="Wiradika",first="Fahmi",middle="Wahyu")

########## Nested Fuction Calls
# num = input("Enter a number : ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)
#
# print(round(abs(float(input("Enter a number : ")))))

########## Scope
# name = "Fahmi"          # global scope (available inside & outside functions)
# def display_name():
#     name = "Waz"        # local scope (variable only inside this function)
#     print(name)
#
# display_name()
# print(name)

############ args
# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[5] = 0
#     for i in stuff:
#         sum += i
#     return sum
#
# print(add(1,2,3,4,5,6))

############ kwargs
# def hello(**names):
#     # print("Hello "+kwargs['first']+" "+kwargs['last'])
#     print("Hello", end=" ")
#     for key,value in names.items():
#         print(value, end=" ")
#
# hello(tittle="Mr.",first="Fahmi",last="Wazza",middle="Calma")

######### str.format
# animal = "cow"
# item = "moon"
# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal,item))
# print("The {1} jumped over the {0}".format(animal,item))      # positional argument
# print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))      # keyword argument
#
# text = "The {} jumped over the {}"
# print(text.format(animal,item))

# name = "Waz"
# print("Hello my name is {}".format(name))
# print("Hello my name is {:10}. Nice to meet you ".format(name))
# print("Hello my name is {:<10}. Nice to meet you ".format(name))
# print("Hello my name is {:>10}. Nice to meet you ".format(name))
# print("Hello my name is {:^10}. Nice to meet you ".format(name))

# number1 = 3.14159
# print("the number pi is {}".format(number1))
# print("the number pi is {:.2f}".format(number1))
# print("the number pi is {:.3f}".format(number1))
# number2 = 1000
# print("the number pi is {}".format(number2))
# print("the number pi is {:.3f}".format(number2))
# print("the number pi is {:,}".format(number2))
# print("the number pi is {:b}".format(number2))
# print("the number pi is {:o}".format(number2))
# print("the number pi is {:x}".format(number2))
# print("the number pi is {:X}".format(number2))
# print("the number pi is {:e}".format(number2))
# print("the number pi is {:E}".format(number2))

################## Random method
# import random
# x=random.randint(1,6)
# y=random.random()
# print(x)
# print(y)
#
# myList = ['rock','paper','scissors']
# z=random.choice(myList)
# print(z)
#
# cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
# random.shuffle(cards)
# print()

################## Exception
# try:
#     numerator = int(input("Numb A : "))
#     denomerator = int(input("Numb B : "))
#     res = numerator / denomerator
# except ZeroDivisionError as e:
#     print(e)
#     print("can devide by 0")
# except ValueError as e:
#     print(e)
#     print("enter only number please")
# except Exception as e:
#     print(e)
#     print("something when wrong")
# else:
#     print(res)
# finally:
#     print("this will always executed")

############### basic file detection in python
# import os
# # path = "C:\\Users\\fahmi\\OneDrive\\Desktop\\test.txt"
# path = "C:\\Users\\fahmi\\OneDrive\\Desktop\\folder"
#
# if os.path.exists(path):
#     print("That location existed")
#     if os.path.isfile(path):
#         print("that is a file")
#     elif os.path.isdir(path):
#         print("that is directory")
# else:
#     print("That location doesnt")

############ reading file in python
# try:
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found")

############ writing file in python
# text = "YOOOOOOOOO \nThis is some text\nhave a good day\n"
# # text = "this text was overwritten"
#
# with open('test.txt','w') as file:
#     file.write(text)
#
# text = "have a nice day"
# with open('test.txt','a') as file:
#     file.write(text)

############ Copy file in python
# import shutil
# #copyfile() =   copy content of file
# #copy()     =   copyfile()  +   permission mode + destination can be a directory
# #copy2()    =   copy()  +   copies metadata (file's creation and modification times)
# shutil.copyfile('test.txt','copy.txt') #src.dst

############ Move file using python
# import os
#
# # source = "C:\\Users\\fahmi\\PycharmProjects\\hellloworlde\\copy.txt"
# source = "floder"
# destination = "C:\\Repository\\Python\\Test_Folder\\floder"
#
# try:
#     if os.path.exists(destination):
#         print("there's a file there ")
#     else:
#         os.replace(source,destination)
#         print(source+" was moved")
# except FileNotFoundError:
#     print("file not found")

############# delete file with python
# import os
# import shutil
# path = "isi"
#
# try:
#     # os.remove(path)       # delete a file
#     # os.rmdir(path)        # delete an empty directory
#     shutil.rmtree(path)     # delete a directory containing  files
# except FileNotFoundError:
#     print("file not found")
# except PermissionError:
#     print("not-auth")
# except OSError:
#     print(" you cannot delete that using that function")
# else:
#     print(path+" was deleted ")

############## module (file containing python code)
# import pesan as P
# P.Hello()
# P.Bye()

# from  pesan import Hello,Bye
# Hello()
# Bye()

# from  pesan import *
# Hello()
# Bye()

# help("modules")     # all module in pyhton build-in

################## QUIZZZZ make rock paper scissors game in python
# import random
#
# while True:
#     tangan = ["watu","kertas","gunting"]
#     computer = random.choice(tangan)
#     player = None
#
#     while player not in tangan:
#         player = input("watu, kertas, gunting? : ").lower()
#
#     if player == computer:
#         print("Computer :",computer)
#         print("Player :",player)
#         print("seri")
#     elif player == "watu":
#         if computer == "kertas":
#             print("Computer :", computer)
#             print("Player :", player)
#             print("kalah")
#         if computer == "gunting":
#             print("Computer :", computer)
#             print("Player :", player)
#             print("menang")
#     elif player == "kertas":
#         if computer == "watu":
#             print("Computer :", computer)
#             print("Player :", player)
#             print("menang")
#         if computer == "gunting":
#             print("Computer :", computer)
#             print("Player :", player)
#             print("kalah")
#     elif player == "gunting":
#         if computer == "kertas":
#             print("Computer :", computer)
#             print("Player :", player)
#             print("menang")
#         if computer == "watu":
#             print("Computer :", computer)
#             print("Player :", player)
#             print("kalah")
#
#     play_again = input("Play again ? ( Y / N ) :")
#
#     if play_again !="Y":
#         break
#
# print("BYE!!")

################## QUIZZ GAMEE
# def new_game():
#     jawab = []
#     jawab_benar = 0
#     nomor_soal = 1
#
#     for key in pertanyaan:
#         print("------------------")
#         print(key)
#         for i in jawaban[nomor_soal-1]:
#             print(i)
#         tebakan = input(" Enter (A, B, C, D): ")
#         tebakan=tebakan.upper()
#         jawab.append(tebakan)
#
#         jawab_benar += check_answer(pertanyaan.get(key),tebakan)
#         nomor_soal += 1
#
#     display_score(jawab_benar,jawab)
#
# # ------------------
# def check_answer(jawaban,tebakan):
#     if  jawaban == tebakan:
#         print("benarr")
#         return 1
#     else:
#         print("salahh")
#         return 0
# # ------------------
# def display_score(jawab_benar,jawab):
#     print("-------------------")
#     print("------Hasil--------")
#     print("-------------------")
#
#     # print("Jawaban : ", end="")
#     for i in pertanyaan:
#         print(pertanyaan.get(i),end=" ")
#     print()
#
#     print("Jawab   : ", end="")
#     for i in jawab:
#         print(i,end=" ")
#     print()
#
#     score = int((jawab_benar/len(pertanyaan))*100)
#     print("your score is "+str(score)+"%")
# # ------------------
# def play_again():
#     response = input(" Do you want to play again? Y / N : ")
#     response = response.upper()
#
#     if response == "Y":
#         return True
#     else:
#         return False
# # ------------------
#
# pertanyaan = {
#     "Ultah micuq adalah ? ": "C",
#     "Tanggal tunangan ? ": "A",
#     "Mas Kawin ? ": "B",
#     "makanan favorit ticuq ? ":"D"
# }
#
# jawaban = [
#     ["A. 22 Mei 1996","B. 23 Mei 1996","C. 24 Mei 1996","D. 25 Mei 1996"],
#     ["A. 28 Agustues 2022","B. 29 Agustues 2022","C. 30 Agustues 2022","D. 27 Agustues 2022"],
#     ["A. Emas 5 gram","B. Emas 10 gram","C. Emas 15 gram","D. Emas 5 kilogram"],
#     ["A. Tahu Khepell","B. Djamure Krispiye","C. Tungkule Kecape","D. semua benar"]
# ]
#
# new_game()
#
# while play_again() :
#     new_game()
#
# print("BYEE!!!")

################# Object Orientation Programming in python
# from car import Car
#
# car_1 = Car("Honda","Civic","2024","Black")
# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)
# car_1.drive()
# car_1.stop()
#
# car_2 = Car("Jeep","Wrangler","2020","Camo")
# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)
# car_2.drive()
# car_2.stop()

############## Basic Class variable in python
# from car import Car
#
# car_1 = Car("Honda","Civic","2024","Black")
# car_2 = Car("Jeep","Wrangler","2020","Camo")
#
# car_2.wheels = 6    #   specific object
# Car.wheels = 7      #   class object
#
# print(car_1.wheels)
# print(car_2.wheels)

############# inherit class in python
# class Animal:
#     alive = True
#
#     def eat(self):
#         print("this animal is eating")
#
#     def sleep(self):
#         print(("this animal is sleeping"))
#
# class Rabbit(Animal):
#     def run(self):
#         print("this rabbit is running")
# class Fish(Animal):
#     def swim(self):
#         print("this fish is swimming")
# class Hawk(Animal):
#     def fly(self):
#         print("this hawk is flying")
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# # print(rabbit.alive)
# # fish.sleep()
# # hawk.eat()
#
# rabbit.run()
# fish.swim()
# hawk.fly()

############### multi-level inheritance in python
#
# class Organism:
#     alive = True
#
# class Animal(Organism):
#     def eat(self):
#         print("this animal is eating")
#
# class Cat(Animal):
#     def meow(self):
#         print("this cat is meowing")
#
# cat = Cat()
# print(cat.alive)
# cat.eat()
# cat.meow()

######### multiple inheritance works in python
#
# class Prey:
#     def flee(self):
#         print("ngibrittt")
#
# class Predator:
#     def hunt(self):
#         print("pantawww")
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey,Predator):
#     pass
#
# klinci = Rabbit()
# e_lang = Hawk()
# iwak = Fish()
#
# klinci.flee()
# e_lang.hunt()
# iwak.hunt()
# iwak.flee()

################## method over writing in python
# class Animal:
#     def eat(self):
#         print("this animal is eating")
#
# class Rabbit:
#     def eat(self):
#         print("this rabbit is eating carrot")
#
# klinci = Rabbit()
# klinci.eat()

############ method chaining in python
# class Car:
#
#     def turn_on(self):
#         print("urip")
#         return self
#
#     def drive(self):
#         print("gass")
#         return self
#
#     def brake(self):
#         print("remm")
#         return self
#
#     def turn_off(self):
#         print("mati")
#         return self
#
# sedan = Car()
# # sedan.turn_on().drive()
# # sedan.brake().turn_off()
# # sedan.turn_on().drive().brake().turn_off()
#
# (sedan.turn_on()
#  .drive()
#  .brake()
#  .turn_off())

############### super function in python
#
# class Rectangle:
#     def __init__(self, panjang, lebar):
#         self.panjang = panjang
#         self.lebar = lebar
#
# class Square(Rectangle):
#     def __init__(self,panjang,lebar):
#         super().__init__(panjang,lebar)
#
#     def area(self):
#         return self.panjang*self.lebar
#
# class Cube(Rectangle):
#     def __init__(self,panjang,lebar,tinggi):
#         super().__init__(panjang,lebar)
#         self.tinggi = tinggi
#
#     def volume(self):
#         return self.panjang*self.lebar*self.tinggi
#
# kotak = Square(3,3)
# kardus = Cube(3,3,3)
#
# print(kotak.area())
# print(kardus.volume())

################ abstract Classes in python
# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
# class Car(Vehicle):
#     def go(self):
#         print("Gassss")
#
#     def stop(self):
#         print("REMMM")
#
#
# class Motorcycle(Vehicle):
#     def go(self):
#         print("Pancallllll")
#
#     def stop(self):
#         print("rem")
#
# # kendaraan = Vehicle()
# mobil = Car()
# speda = Motorcycle()
#
# mobil.go()
# speda.go()
#
# mobil.stop()
# speda.stop()

####################### How to pass object as argument in Python
# class Car:
#     color=None
#
# class Motorcycle:
#     color=None
# def change_color(kendaraan,color):
#     kendaraan.color = color
#
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
# speda1= Motorcycle()
# speda2= Motorcycle()
# speda3= Motorcycle()
#
# change_color(car_1,"black")
# change_color(car_2,"white")
# change_color(car_3,"blue")
# change_color(speda1,"ireng")
# change_color(speda2,"abang")
# change_color(speda3,"abu")
#
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(speda1.color)
# print(speda2.color)
# print(speda3.color)

############### Duck Typing in Python
# class Duck:
#     def walk(self):
#         print("wek wek mlaku")
#
#     def talk(self):
#         print("wek wek wek wek")
#
# class Chicken:
#     def walk(self):
#         print("ptok ptok mlaku")
#
#     def talk(self):
#         print("ptok ptok ptok ptok")
#
# class Person():
#     def catch(self, Wekk):
#         Wekk.walk()
#         Wekk.talk()
#         print("entuk wek wek wek")
#
# wek = Duck()
# ptok = Chicken()
# wong = Person()
#
# wong.catch(wek)
# wong.catch(ptok)

################## Walrus Operator
# happy = False
# print(happy := True)
#
# foods = list()
# # while True:
# #     food = input("Karo opo mase? : ")
# #     if food == "wes":
# #         break
# #     foods.append(food)
#
# while food := input("karo opo mase? : ")!= "wes":
#     foods.append(food)

###### Assign Function to variable in python
# def Hello():
#     print("Hello")
#
# Hello()
# print(Hello)
# hi = Hello
# print(hi)
# hi()

# say = print
# say("hahahahahaha")

############ higher order function in python
# def loud(text):
#     return text.upper()
#
# def quiet(text):
#     return text.lower()
#
# def hello(func):
#     text = func("Hello")
#     print(text)
#
# hello(loud)
# hello(quiet)

# def divisor(x):
#     def devidend(y):
#         return y / x
#     return devidend
#
# devide = divisor(2)
# print(devide(10))

################ Lambda function in Python
# lambda parameter:expression
# def double(x):
#     return x * 2
#
# print(double(5))

# double = lambda x:x*2
# multiply = lambda x, y: x*y
# add = lambda  x,y,z:x+y+z
# full_name = lambda name1,name2 : name1+" "+name2
# age_check = lambda age: True if age >= 18 else False
#
# print(double(5))
# print((multiply(2,5)))
# print(add(4,4,2))
# print(full_name("Fahmi","Wazza"))
# print(age_check(19))

############ sort data in pyhton
# student1 = ["Squidward","Spongebob","Mr.Krabs","Patrick","Sandy"]    #list
# student2 = ("Squidward","Spongebob","Mr.Krabs","Patrick","Sandy")    #tuple
#
# student1.sort()
# for i in student1:
#     print(i)
# student1.sort(reverse=True)
# for i in student1:
#     print(i)

# sorted_student2 = sorted(student2)
# for i in sorted_student2:
#     print(i)
# sorted_student2 = sorted(student2,reverse=True)
# for i in sorted_student2:
#     print(i)

# students1 = [
#     ("Squidward","C",40),
#     ("Spongebob","B",38),
#     ("Patrick","E",39),
#     ("Sandy","A",28),
#     ("Mr.Krabs","D",50)
# ]
# students2 = (
#     ("Squidward","C",40),
#     ("Spongebob","B",38),
#     ("Patrick","E",39),
#     ("Sandy","A",28),
#     ("Mr.Krabs","D",50)
# )
#
# grade = lambda grades:grades[1]
# age = lambda ages:ages[2]
# # students1.sort(key=age)
# sorted_student = sorted(students2,key=grade)
# for i in sorted_student:
#     print(i)

############## map function in python
# map(function, iterable)
# toko = [
#     ("jaket", 180000.00),
#     ("kaos", 75000.00),
#     ("flanel", 100000.00),
#     ("jean", 90000.00),
# ]
#
# to_yen = lambda data: (data[0],data[1]*0.0092)
# to_usd = lambda data: (data[0],data[1]*0.000065)
#
# toko_jp = list(map(to_yen, toko))
# toko_us = list(map(to_usd, toko))
#
# print("Toko JP")
# for i in toko_jp:
#     print(i)
# print("Toko US")
# for i in toko_us:
#     print(i)

############# filter function in python
# murid = [
#     ("Agus", 78),
#     ("Bambang", 65),
#     ("Cahyo", 85),
#     ("Dedy", 92),
#     ("Eka", 81),
# ]
# kkm = lambda nilai:nilai[1]>=80
# Lulus = list(filter(kkm,murid))
# for i in Lulus:
#     print(i)

############# Reduce function
# import functools
# letters = ["F","A","H","M","I"," ","W","A","Z","Z","U"]
# nama = functools.reduce(lambda x , y :x+y,letters)
# print(nama)
# factorial = [5,4,3,2,1]
# hasil = functools.reduce(lambda x , y : x*y, factorial)
# print(hasil)

########### List Comprehension in Python
# square = []
# for i in range(1,11):
#     square.append(i*i)
# print(square)
#
# squares = [i * i for i in range(1,11)]
# print(squares)
#
# murid = [100,0,90,10,80,20,70,30,60,40,50]
# # lulus = list(filter(lambda x : x>=60 , murid))
# # lulus = [i for i in murid if i >=60]
# lulus = [i if i >=60 else "GAGAL" for i in murid]
# print(lulus)

########### Dictionary Comprehension in Python
### Converting value to new value in dictionary
# cities_in_F = {'New York':32,'Boston':75,'Los Angeles':100,'Chicago':50}
# cities_in_C = {key: round((value-32)*(5/9)) for(key,value) in cities_in_F.items()}
# print(cities_in_C)
### Selecting sunny weather from dictionary
# weather = {'New York':"Snowing",'Boston':"Sunny",'Los Angeles':"Sunny",'Chicago':"Cloudy"}
# sunny_weather = {key : value for (key,value) in weather.items() if value=="Sunny"}
# print(sunny_weather)
### Selecting if/else in dictionary
# cities = {'New York':32,'Boston':75,'Los Angeles':100,'Chicago':50}
# desc_cities = {key : ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)
### Replace if/else with function in dictionary
# def check_suhu(value):
#     if value >=70:
#         return "HOT"
#     elif 60 >= value >= 40:
#         return "Warm"
#     else:
#         return "COLD"
#
# cities = {'New York':32,'Boston':75,'Los Angeles':100,'Chicago':50}
# desc_cities = {key : check_suhu(value) for (key,value) in cities.items()}
# print(desc_cities)

############# zip (iterable)
# usernames = ["Dude","Bro","Mister"]
# password = ("1234","5678","qwert")
# login_date = ["1/1/2021","1/2/2021","1/3/2021"]
#
# users = zip(usernames, password,login_date)
#
# print(type(users))
#
# for i in users:
#     print(i)

########## if __name__ == '__main__' in python
# def hello():
#      print("Hello!")
#
# if __name__ == "__main__":
#     hello()
#     # print("Running this main directly")
# else:
#     print("Running other module indirectly")

######### Time Module in Python
# import time

# print(time.ctime(1000000)) # epoch = when your computer thinks time began
# print(time.time())   # return current seconds since epoch
# print(time.ctime(time.time())) # get current date/time

# time_object = time.localtime()
# # time_object = time.gmtime()
# print(time_object)
# local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)
# print(local_time)

# time_string = "20 February, 1997"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)

# # (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)
#
# # (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)

# ############# Multithreading i Python
# import threading
# import time
#
# def eat():
#     time.sleep(3)
#     print("mangan")
#
# def drink():
#     time.sleep(4)
#     print("ngombe")
#
# def study():
#     time.sleep(5)
#     print("sinau")
#
# x = threading.Thread(target=eat,args=())
# x.start()
#
# y = threading.Thread(target=drink,args=())
# y.start()
#
# z = threading.Thread(target=study,args=())
# z.start()
#
# x.join()
# y.join()
# z.join()
#
# # eat()
# # drink()
# # study()
#
# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())

########## Deamon Thread

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for : ",count," seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)



answer = input("Do you want to exit?")







































































































































































































