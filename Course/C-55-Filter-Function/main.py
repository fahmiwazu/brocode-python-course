############# filter function in python
murid = [
    ("Agus", 78),
    ("Bambang", 65),
    ("Cahyo", 85),
    ("Dedy", 92),
    ("Eka", 81),
]
kkm = lambda nilai:nilai[1]>=80
Lulus = list(filter(kkm,murid))
for i in Lulus:
    print(i)