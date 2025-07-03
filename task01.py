import json
students = [
    {"name": "Ali", "surname": "Valiyev", "age": 20},
    {"name": "Laylo", "surname": "Karimova", "age": 21},
    {"name": "Bekzod", "surname": "Xolmatov", "age": 19}
] 


with open("students.json", "w") as jsonfile:
    json.dump(students, jsonfile, indent=4)
    
# with open("students.json", "r") as jsonfile:
#     data = json.load(jsonfile)

# for i in data:
#     print(i["name"])

