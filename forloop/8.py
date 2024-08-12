#  Prime Number Checker
# Problem: Check if a number is prime.

n=int(input("Enter the  number :"))
if n==2:
    print("prime number ")
else:
    for i in range (2,n):
        if n%i==0:
            print("not a prime factor ")
            break
        else:
            print("prime number ")
            break
