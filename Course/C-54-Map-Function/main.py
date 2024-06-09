############## map function in python
# map(function, iterable)
toko = [
    ("jaket", 180000.00),
    ("kaos", 75000.00),
    ("flanel", 100000.00),
    ("jean", 90000.00),
]

to_yen = lambda data: (data[0],data[1]*0.0092)
to_usd = lambda data: (data[0],data[1]*0.000065)

toko_jp = list(map(to_yen, toko))
toko_us = list(map(to_usd, toko))

print("Toko JP")
for i in toko_jp:
    print(i)
print("Toko US")
for i in toko_us:
    print(i)