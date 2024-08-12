import random
import string 

l=(int(input("Enter the length of password  :")))
n= input("Do you want to include numbers? (yes/no): ").lower() in ['yes', 'y']
s= input("Do you want to include special characters? (yes/no): ").lower() in ['yes', 'y']

rand_d=random.choice(string.digits)
rand_scc=random.choice(string.punctuation)
rand_lcc=random.choice(string.ascii_lowercase)
rand_ucc=random.choice(string.ascii_uppercase)

temp=rand_d+rand_scc+rand_lcc+rand_ucc
e=""
# for i in range (l):
#     if 
#     e+=random.choice(temp)
# print(e)

