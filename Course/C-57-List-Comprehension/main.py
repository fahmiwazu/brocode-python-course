########### List Comprehension in Python
square = []
for i in range(1,11):
    square.append(i*i)
print(square)

squares = [i * i for i in range(1,11)]
print(squares)

murid = [100,0,90,10,80,20,70,30,60,40,50]
# lulus = list(filter(lambda x : x>=60 , murid))
# lulus = [i for i in murid if i >=60]
lulus = [i if i >=60 else "GAGAL" for i in murid]
print(lulus)