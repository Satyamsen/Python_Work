# Exercise 4: Initialize dictionary with default values

#     employees = ['Kelly', 'Emma']
#     defaults = {"designation": 'Developer', "salary": 8000}

#     Output: 
#     {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
l=dict.fromkeys (employees,defaults)
print(l)