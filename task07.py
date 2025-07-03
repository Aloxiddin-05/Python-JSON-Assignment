import json

with open("students.json",) as jsonfile:
    data = json.load(jsonfile)

    
    jami =0
    soni = 0
    for i in data:
        jami += i["age"]
        soni += 1
    print(jami/soni)