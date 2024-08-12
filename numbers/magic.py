# 1729, the Hardy-Ramanujan Number, is the smallest number which can be expressed as the sum of two different cubes in two different ways. 1729 is the sum of the cubes of 10 and 9 - cube of 10 is 1000 and cube of 9 is 729; adding the two numbers results in 1729

def magic(n):
    a=0
    for i in range(0,n):
        a=a+i
        b=a+1
        if a**3 + b**3 == n:
            return print("magic number")
        else:
            return print("not magic number")


a=int(input("enter your nummber"))
magic(a)
