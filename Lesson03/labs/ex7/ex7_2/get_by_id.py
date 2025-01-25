import requests
import json
import os
import sys


userId = int(input("Enter user id: "))

resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{userId}')
data = resp.json()
user = {"name": data["name"], "email": data["email"]}
print(user)

if user["name"].startswith("E"):
    resp = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={userId}')
    data = resp.json()
    titles = list(map(lambda x: x["title"], data))

    with open(os.path.join(sys.path[0], "titles.json"), 'w') as f:
        json.dump({"titles": titles}, f)
        f.close()

    # f = open("Lesson03/labs/ex7/ex7_2/titles.json", 'w')

    # json.dump({"titles": titles}, f)

    # f.close()
