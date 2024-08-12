# def integer(x = 0 ,y = 0):
#     #x,y=map(int,input().split())
#     a=x+y+1
#     return a
# print(integer())


# def naam(x,y):
#     a=print(x+y)
#     return a
# x,y=(list(input().split()))
# naam(x,y)
# def greed_hye(x):
#     a=x+"hye"
#     return print(a)
# n=(input(""))
# greed_hye(n)
def parent(num):
    # print("I am sanjay")
    
    def child_1():
        return("I am satyam")

    def child_2():
        return("I am sahil")
    
    if num==1:
        return child_1
    elif num==2 :
        return child_2

first=parent(1)
second=parent(2)
print(first())
print(second())