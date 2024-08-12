# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

n=input("Enter the String :")
for i in n:
    c=n.count(i)
    if c==1:
        print(i)
        break