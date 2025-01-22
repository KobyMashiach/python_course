student = {
    "name": "Avi",
    "age": 30,
    "grades": [90, 88, 100],
    "address":
        {
            "city": "Eilat",
            "street":
                {
                    "name": "Herzel",
                    "no": 20,
                }
    }
}


# Get the name
print(student["name"])

# Get the street name
print(student["address"]["street"]["name"])
