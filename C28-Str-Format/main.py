######### str.format
animal = "cow"
item = "moon"
print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item))      # positional argument
print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))      # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal,item))

name = "Waz"
print("Hello my name is {}".format(name))
print("Hello my name is {:10}. Nice to meet you ".format(name))
print("Hello my name is {:<10}. Nice to meet you ".format(name))
print("Hello my name is {:>10}. Nice to meet you ".format(name))
print("Hello my name is {:^10}. Nice to meet you ".format(name))

number1 = 3.14159
print("the number pi is {}".format(number1))
print("the number pi is {:.2f}".format(number1))
print("the number pi is {:.3f}".format(number1))
number2 = 1000
print("the number pi is {}".format(number2))
print("the number pi is {:.3f}".format(number2))
print("the number pi is {:,}".format(number2))
print("the number pi is {:b}".format(number2))
print("the number pi is {:o}".format(number2))
print("the number pi is {:x}".format(number2))
print("the number pi is {:X}".format(number2))
print("the number pi is {:e}".format(number2))
print("the number pi is {:E}".format(number2))