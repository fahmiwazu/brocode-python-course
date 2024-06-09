############### super function in python

class Rectangle:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

class Square(Rectangle):
    def __init__(self,panjang,lebar):
        super().__init__(panjang,lebar)

    def area(self):
        return self.panjang*self.lebar

class Cube(Rectangle):
    def __init__(self,panjang,lebar,tinggi):
        super().__init__(panjang,lebar)
        self.tinggi = tinggi

    def volume(self):
        return self.panjang*self.lebar*self.tinggi

kotak = Square(3,3)
kardus = Cube(3,3,3)

print(kotak.area())
print(kardus.volume())