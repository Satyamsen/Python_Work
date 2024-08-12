# Exercise 6: Delete a list of keys from a dictionary
    
#     sample_dict = {
#         "name": "Kelly",
#         "age": 25,
#         "salary": 8000,
#         "city": "New york"
#     }

#     # Keys to remove
#     keys = ["name", "salary"]

#     Output: 
#     {'city': 'New york', 'age': 25}

sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
}
keys = ["name", "salary"]

# del sample_dict['name']
# del sample_dict['salary']
# print(sample_dict)

for i in keys:
    del sample_dict[i]
print(sample_dict)
    
    