import pymongo 

cl=pymongo.MongoClient("mongodb://localhost:27017")
database=cl["Students"]
table=database["name"]

