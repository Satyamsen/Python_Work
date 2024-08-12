# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop


# def fun(n):
#     a=n*(n-1)*fun(n)
#     n=n-1
#     if n==0:
#         return print(a)

# fun(int(input("Enter the n umbers :")))

n=int(input("Enter the n umbers :"))
a=1
while n>=1:
    a=n*a
    n=n-1
    
print(a)

