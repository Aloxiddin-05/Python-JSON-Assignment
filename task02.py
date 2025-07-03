import json

with open("students.json","r") as jsonfile:
    data = json.load(jsonfile)
    
    
    for i in data:
        print(f"{i['name']} - {i['age']} yosh")
    
    