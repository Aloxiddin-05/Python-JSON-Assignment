import json
with open("students.json") as jsonfile:
    data = json.load(jsonfile)

    maksimal_user = data[0]
    for user in data:
        if maksimal_user["age"] < user["age"]:
            maksimal_user = user
            
print(maksimal_user)
