import json

with open("students.json") as jasonfile:
    data = json.load(jasonfile)
    
    userlar_soni = len(data)
print(userlar_soni)