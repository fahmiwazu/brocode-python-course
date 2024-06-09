############ sort data in pyhton
student1 = ["Squidward","Spongebob","Mr.Krabs","Patrick","Sandy"]    #list
student2 = ("Squidward","Spongebob","Mr.Krabs","Patrick","Sandy")    #tuple

student1.sort()
for i in student1:
    print(i)
student1.sort(reverse=True)
for i in student1:
    print(i)

sorted_student2 = sorted(student2)
for i in sorted_student2:
    print(i)
sorted_student2 = sorted(student2,reverse=True)
for i in sorted_student2:
    print(i)

students1 = [
    ("Squidward","C",40),
    ("Spongebob","B",38),
    ("Patrick","E",39),
    ("Sandy","A",28),
    ("Mr.Krabs","D",50)
]
students2 = (
    ("Squidward","C",40),
    ("Spongebob","B",38),
    ("Patrick","E",39),
    ("Sandy","A",28),
    ("Mr.Krabs","D",50)
)

grade = lambda grades:grades[1]
age = lambda ages:ages[2]
# students1.sort(key=age)
sorted_student = sorted(students2,key=grade)
for i in sorted_student:
    print(i)