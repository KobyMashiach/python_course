import requests

# Get all users
resp = requests.get('https://jsonplaceholder.typicode.com/users')
data = resp.json()
# print(data)

# for per in data:
#     print(per["name"])


# Get 1 user
resp = requests.get('https://jsonplaceholder.typicode.com/users/3')
data = resp.json()
# print(data)

# Send new user
obj = {"name": "Ron", "email": "ron@gmail.com"}
resp = requests.post('https://jsonplaceholder.typicode.com/users', obj)
# print(resp.json())

# Update  user
obj = {"name": "Ron1", "email": "ron1@gmail.com"}
resp = requests.put('https://jsonplaceholder.typicode.com/users/3', obj)
# print(resp.json())


# Delete new user
resp = requests.delete('https://jsonplaceholder.typicode.com/users/3')
print(resp.json())
