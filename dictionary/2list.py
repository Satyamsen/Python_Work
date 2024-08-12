
a=["apple","banana","mango","orange"]
b=["apple jucice","banana shake","mango shake","orange juice"]
c={}
for (i,j) in zip(a,b):
    c[i]=j
print(c)