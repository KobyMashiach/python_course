import json

student = {}
student["id"] = 1
student["name"] = "Ron"
student["faculty"] = {}
student["faculty"]["profession"] = "Math"
student["faculty"]["grade"] = 90

f = open("Lesson03/demos/demo01_access_json_files/student_from_code.json", 'w')

json.dump(student, f)

f.close()
