from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(port=27017)
db = client["personsDB"]
persons_collection = db["persons"]

# ! Get all recored from persons collection
pers = persons_collection.find({})  # select * from persons
# for per in pers:
#     print(per)

# ! Get 1 person by his _id
person = persons_collection.find_one(
    {"_id": ObjectId("67943d58ec897b899c625d13")})
# print(person)

# ! Create person
# obj = {"FirstName": "Gil", "LastName": "Lavie"}
# persons_collection.insert_one(obj)

# objList = [{"FirstName": "Gil", "LastName": "Lavie"},
#            {"FirstName": "Gil", "LastName": "Lavie"}]
# persons_collection.insert_many(objList)

# ! Update person
# obj = {"FirstName": "Gil1", "LastName": "Lavie1"}
# persons_collection.update_one(
#     {"_id": ObjectId("67943f523307aaecbb6c2486")}, {"$set": obj})

# ! Update all persons
# obj = {"city": "Jerusalem"}
# persons_collection.update_many({"city": "Ashdod"}, {"$set": obj})


# ! Delete personby his _id
# persons_collection.delete_one({"_id": ObjectId("67943feada2d2c37d6b8adf2")})
