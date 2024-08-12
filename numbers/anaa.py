n=int(input("Enter the Number :"))

# for i in range (0,n+1):
#     print(i,(n+1)-1)
#     n=n-1

for (i,j) in zip(range(0,n+1),range(n,-1,-1)):
    print(i,j)


#     for j in range (0,n):
#         j=j[::-1]
# print(i,j)