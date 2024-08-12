class WorkingWithAttributes:
    pi = 3.14
    def __init__(self,radius, height):
        self.radius = radius
        self.height = height
    def volume(self):
        return self.pi*(self.radius**2)*self.height
a = WorkingWithAttributes(2,6)
print(a.volume())

