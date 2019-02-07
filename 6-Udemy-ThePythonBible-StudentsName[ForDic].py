#loops in dictionaries
students= {
    "male": ["Tom", "CHarlie", "Harry", "Frank"],
    "female" : ["Sarah", "Hunda", "Samantha", "Emily", "Elizabeth"]
}
# print names who have "a"
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
