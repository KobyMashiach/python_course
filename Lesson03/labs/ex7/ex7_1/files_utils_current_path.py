import json
import os
import sys


def getPersonData(street):

    with open(os.path.join(sys.path[0], "persons.json"), 'r') as f:
        data = json.load(f)
        f.close()

    pers = data["persons"]
    newPersons = []
    for p in pers:
        if p["Address"]["Street"]["Name"] == street:
            obj = {"name": p["Name"], "city": p["Address"]
                   ["City"], "street": f"{p["Address"]["Street"]["Name"]} {p["Address"]["Street"]["Number"]}"}
            newPersons.append(obj)
    return newPersons


persons = getPersonData("Ben Yehuda")
print(persons)
