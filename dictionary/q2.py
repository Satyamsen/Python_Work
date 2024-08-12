# Exercise 2: Merge two Python dictionaries into one

#     dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#     dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

#     Output: 
#     {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 ={}

for (i,j) in zip(dict1,dict2):
    dict3[i]=dict1[i]
    dict3[j]=dict2[j]
print(dict3)

