# Exercise 8: Rename key of a dictionary

#     sample_dict = {
#         "name": "Kelly",
#         "age":25,
#         "salary": 8000,
#         "city": "New york"
#     }

#     Output: 
#     {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

sample_dict = {
        "name": "Kelly",
        "age":25,
        "salary": 8000,
        "city": "New york"
    }
a=sample_dict.pop('city')
print(a)
newdict={'location':a}
sample_dict.update(newdict)
print(sample_dict)


