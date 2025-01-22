col = {3: "Avi", 6: "Dana", 9: "Ron", "AA": 100}

# Print all dictionary
print(col)

print(col[3])
print(col["AA"])

# Replace existing value with a new one
col[3] = "Aviva"
print(col)

#  Add a new key-value pair
col[7] = "Dganit"
print(col)

# Get all keys
keys = list(col.keys())

# check if key exist
if 6 in keys:
    print('exist')

values = list(col.values())
print(values)

# Delete key-pair
del col[6]
