#  2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

# n=int(input("Enter the n umbers :"))
# c=0
# for i in range (1,n+1):
#     if i%2==0:
#         c+=i
# print(c)

n=int(input("Enter the n umbers :"))
c=0
for i in range (0,n+1,2):
    #if i%2==0:
    c+=i
print(c)