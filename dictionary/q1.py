# Exercise 1: Convert two lists into a dictionary
    
#     keys = ['Ten', 'Twenty', 'Thirty']
#     values = [10, 20, 30]

#     Output: 
#     {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dictionary={}
for (i,j) in zip(keys,values):
    my_dictionary[i]=j
print(my_dictionary)