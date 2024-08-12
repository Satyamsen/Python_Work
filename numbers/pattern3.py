#! python3

from sys import argv 
tool_name,file=argv
p=open(file).read()
s=0
sp=0
t=0
v=0
for i in str(p):
    if i==" ":
        s+=1
print(s)