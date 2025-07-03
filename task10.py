import json

with open("students.json") as jsonfile:
    data = json.load(jsonfile)
    
    
    sortlangan = sorted(data,key=lambda x:int(x["age"]))
    print(sortlangan)