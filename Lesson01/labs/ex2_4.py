col = {
    "nums": [77, 95],
    "Student": {
        "Name": "Avi",
        "ID": 111111,
        "Grades": {
            "score": [89, 96, 100]
        }
    }
}

nums = col["nums"]
score = col["Student"]["Grades"]["score"]

numsAvg = sum(nums)/len(nums)
scoreAvg = sum(score)/len(score)

print(max([numsAvg, scoreAvg]))
