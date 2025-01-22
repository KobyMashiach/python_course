arr = [
    {"id": 1, "name": "Ron"},
    {"id": 2, "name": "Dana"},
    {"id": 3, "name": "Avi"},
]

names = list(map(lambda x: x["name"], arr))
print(names)
