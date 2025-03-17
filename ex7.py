studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

for name in studentNames:
    print(f"{name} Evans")

newname = input("Add another name to the list: ")
studentNames.append(newname)

for name in studentNames:
    print(f"{name} Evans")
