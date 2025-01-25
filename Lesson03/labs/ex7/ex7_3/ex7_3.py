import requests
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(port=27017)
db = client["moviesDB"]
movies_collection = db["movies"]

resp = requests.get("https://api.tvmaze.com/shows")
data = resp.json()

movies_collection.delete_many({})

shows = []
for i in range(10):
    show = {"name": data[i]["name"], "genres": data[i]
            ["genres"], "averageRating": data[i]["rating"]["average"]}
    shows.append(show)
    movies_collection.insert_one(show)

userMoviesName = input("Enter a movie name: ")
movie = movies_collection.find_one(
    {"name": userMoviesName})
newMovieName = input("Enter a new name to this movie: ")
movies_collection.update_one(
    {"_id": ObjectId(movie["_id"])}, {"$set": {"name": newMovieName}})
