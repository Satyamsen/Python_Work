n=int(input("Enter the Range :"))

for i in range(0,n):
    for j in range(0,n+1):
        if(j>i):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()



