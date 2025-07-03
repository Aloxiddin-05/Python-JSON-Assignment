import json

with open("students.json","r") as jsonfile:
    data = json.load(jsonfile)
    
    sort_age = filter(lambda x:x["age"] > 20,data)
    print(list(sort_age))
            