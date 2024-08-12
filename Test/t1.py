# 1. WAP to display :
# *****
# *
# *****
#     *
# *****

# str=""    
# for R in range(0,7):    
#     for C in range(0,7):     
#         if (((R == 0 or R == 3 or R == 6) and C > 1 and C < 5) or (C == 1 and (R == 1 or R == 2 or R == 6)) or (C == 5 and (R == 0 or R == 4 or R == 5))):  
#             str=str+"*"    
#         else:      
#             str=str+" "    
#     str=str+"\n"    
# print(str)

n=5
for r in range(1,6):    
    for c in range(1,6):
        if (r%2)!=0 or (c==1 and r==2 or r==4 and c==5):
            print("*",end="")
        else: 
            print(" ",end="")
    print("\n")

       