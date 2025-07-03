import json

with open("students.json","r") as jsonfile:
    data = json.load(jsonfile)
    
    name = input("name = ")
    surname = input("surname = ")
    age = input("age = ")
    
    full_name_age = ({"name": name, "surname": surname, "age": age})
    
    data.append(full_name_age)
    
with open("students.json","w") as jsonfile:
    json.dump(data,jsonfile,indent=4)