import json
import csv

with open("students.json") as jsonfile:
    data = json.load(jsonfile)
    
    for i in data:
        {"name":i["name"],
         "surname":i["surname"],
         "age":i["age"]
        }
    
with open("students.csv","w") as jsonfile:
    fieldnames = ["name","surname","age"]
    write = csv.DictWriter(jsonfile,fieldnames=fieldnames)
    write.writeheader()
    
    
    for dict in data:
        write.writerow(dict)
    
