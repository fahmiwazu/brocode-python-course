############ Tuple
student = ("Waz",24,"Lanang")
print(student.count("Waz"))
print(student.index("Lanang"))

for x in student:
    print(x)

if "Waz" in student:
    print("Waz is here")