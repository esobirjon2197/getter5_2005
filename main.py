
# 5-m
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.__ram = ram



    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, new_ram):
        self.__ram = new_ram

l = Laptop('HP', 8)
print(l.brand, l.ram)

res = l.ram
print(res)

l.ram = 20
print(l.ram)m
