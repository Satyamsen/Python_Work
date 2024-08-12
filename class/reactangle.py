class reactangle :
    def __init__(self,length ,width):
        self.length=length
        self.width=width
    def area(self):
        return (self.length*self.width)
r=reactangle(2,3)
print(r.area())

# class cube(reactangle):
#     super(__init__(self,length,width)):