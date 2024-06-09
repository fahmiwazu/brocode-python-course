################ Lambda function in Python

#lambda parameter:expression
def double(x):
    return x * 2

print(double(5))

double = lambda x:x*2
multiply = lambda x, y: x*y
add = lambda  x,y,z:x+y+z
full_name = lambda name1,name2 : name1+" "+name2
age_check = lambda age: True if age >= 18 else False

print(double(5))
print((multiply(2,5)))
print(add(4,4,2))
print(full_name("Fahmi","Wazza"))
print(age_check(19))