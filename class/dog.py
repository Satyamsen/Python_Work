class car:
    def __init__(self ,name ,age ):
        self.name = name
        self.age=age
    def mydog(self):
        return f"{self.name,self.age}"
    
my = car("tuktuk",5)
print(my.mydog())

