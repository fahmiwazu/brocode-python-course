############### If Statement
age = int(input("How old are you? : "))

if age == 100:
    print("you are sepuh")
elif age >= 18:
    print("you are an adult")
elif age < 0:
    print("you havent born yet")
else:
    print("You are a child")