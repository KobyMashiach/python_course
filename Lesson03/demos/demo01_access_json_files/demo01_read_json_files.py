import json

# modes:
# 'r' - read
# 'w' - write
# 'a' - append

f = open("Lesson03/demos/demo01_access_json_files/persons.json", 'r')
data = json.load(f)
f.close()

pers = data["persons"]
# print(pers)

for per in pers:
    print(per["name"])
