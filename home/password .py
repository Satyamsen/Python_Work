import random

l=(int(input("Enter the length of password  :")))

d=['0','1','2','3','4','5','6','7','8','9']
scc=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<'] 
lcc= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't','u', 'v', 'w','x', 'y','z'] 
  
ucc= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 

combinelist=d+scc+lcc+ucc

rand_d=random.choice(d)
rand_scc=random.choice(scc)
rand_lcc=random.choice(lcc)
rand_ucc=random.choice(ucc)

temp=rand_d+rand_scc+rand_lcc+rand_ucc
e=""
for i in range (l):
    e+=random.choice(temp)
print(e)