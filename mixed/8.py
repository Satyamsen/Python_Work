# 8.	Find the largest number in a list using a for loop.

# n=(input("enetr the numbers :"))
# l=list(n.split(" "))
# print(l)
# t=0
# for i in l:
#     a=int(i)
#     if a>a:
#         print(a)
# n= ['1', '6', '4', '5', '3', '2', '8']
n=[1,2,3,4,5,6,7,8,9]
t=0
# n.sort
# print(n[-1])
for i in n:
    a=int(i)
    t+=a
    if t>a:
        print(t)