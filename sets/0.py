
a=set(map(int,input().split()))
if 0<(len(set(a)))<501:
    n=int(input())
    if 0<n<21:
        for i in range (n):
            b=set(map(int,input().split()))
            if 0<b<101:
                if a.issuperset(b):
                    print("False")
                    break
                else:
                    print("True")
            
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12