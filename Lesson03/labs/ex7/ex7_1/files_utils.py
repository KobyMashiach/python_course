import json


def getPersonData(street):
    f = open("Lesson03/labs/ex7/ex7_1/persons.json", 'r')
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
