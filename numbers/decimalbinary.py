
def deci(n):
    s=""
    while n>0:
        s=str(n%2)+s
        n=n//2
    return(s)

c=int(input("Enter the Number :"))
print("Binary Number :",deci(c))