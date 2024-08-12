n=int(input().strip())
a=[]
for i in range(n):
    b= input().strip().split()
    if b[0] == "insert":
        a.insert(int(b[1]), int(b[2]))
    elif b[0] == "print":
        print(a)
    elif b[0] == "remove":
        a.remove(int(b[1]))
    elif b[0] == "append":
        a.append(int(b[1]))
    elif b[0] == "sort":
        a.sort()
    elif b[0] == "pop":
        a.pop()
    elif b[0] == "reverse":
        a.reverse()


        
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print