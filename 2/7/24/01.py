lst = [4,4,5,5,4,5,4,4,5,5]
count = 0
n = None
for i in lst:
    if count == 0:
        n = i
    if n == i: count += 1
    else: count -= 1

if count == 0: print("Equal")
else: print(n)