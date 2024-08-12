class Square:

    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side**2
a = Square(4)
print(a.area())

