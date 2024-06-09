############# Reduce function
import functools
letters = ["F","A","H","M","I"," ","W","A","Z","Z","U"]
nama = functools.reduce(lambda x , y :x+y,letters)
print(nama)
factorial = [5,4,3,2,1]
hasil = functools.reduce(lambda x , y : x*y, factorial)
print(hasil)