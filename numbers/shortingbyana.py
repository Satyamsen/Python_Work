my_list=[]
while True:
    a=(input())
    if a=="":
        break
    else: my_list.append(int(a))

for i in range(len(my_list)):
    for j in range(len(my_list)):
        if my_list[i]>my_list[i+1]:
            my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
        else:
            pass
    