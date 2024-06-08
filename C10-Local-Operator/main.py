############## Logical Operator
temp = int(input("What's the temperature outside? : "))

if not (temp <= 0 and temp >= 30):
    print("wokayyy")
elif not (temp > 0 or temp < 30):
    print("nayyy")