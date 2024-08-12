# Exercise 5: Create a dictionary by extracting the keys from a given dictionary

#     sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

#     # Keys to extract
#     keys = ["name", "salary"]

#     Output: 
#     {'name': 'Kelly', 'salary': 8000}

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]
v={}
for i in keys:
   v[i]=sample_dict[i]
print(v)
