import json

name = "sadegh"
familyName = "khoshbayan"
marks = {"riyazi": [20, 14, 12], "fizik": [20, 15, 13]}
sex = None
d = {"name": name, "familyName": familyName, "marks": marks, "sex": sex}
with open("jsonfile.json", "w") as jf:
    json.dump(d,jf,indent=4)

with open("jsonfile.json", "r") as jf:
    j = json.load(jf)
mark_fizik = j["marks"]["fizik"]
print(mark_fizik)
