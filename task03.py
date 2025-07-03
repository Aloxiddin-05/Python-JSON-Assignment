import json

with open("students.json") as jsonfile:
    data = json.load(jsonfile)
    
    data.append({"name": "Shahzoda", "surname": "Nazarova", "age": 22})

with open("students.json","w") as jsonfile:
    json.dump(data,jsonfile,indent=4)
