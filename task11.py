import os
import json

if not os.path.exists("students.json"):
    with open("students.json","w") as jsonfile:
        jsonfile.write("[]")