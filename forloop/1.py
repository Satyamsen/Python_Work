# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
c=0
for i in numbers:
    if i>=0:
        c+=1
print(c)

