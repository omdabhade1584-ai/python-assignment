students={
    101:{"Name":"Akash", "Scores":[10,20,45]},
    102:{"Name":"Varun", "Scores":[89,20,78]},
    103:{"Name":"Ram", "Scores":[80,67,84]},
    104:{"Name":"Yash", "Scores":[56,70,85]},
    105:{"Name":"Om", "Scores":[78,74,85]},
}

for sid, details in students.items():
    avg=sum(details["Scores"])/len(details["Scores"])
    details["Average"] = avg
    details["Passed"] = avg >= 30

print("Students who passed:")
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"])