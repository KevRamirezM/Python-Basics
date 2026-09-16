# Writing files in python
import json
import csv

# Strings
data = "Hello world"

file_path = "Harder Topics/files/output.txt"

with open(file_path, "w") as file:
    file.write(data)
    print(f"Text is created in '{file_path}'")

# Lists
words = ["pizza", "watermelon", "strawberry", "banana"]

file_path2 = "Harder Topics/files/output2.txt"

with open(file_path2, "w") as file:
    for word in words:
        file.write(data + "\n")
    print(f"Text is created in '{file_path2}'")

# JSON
employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path3 = "Harder Topics/files/output3.json"

with open(file_path3, "w") as file:
    json.dump(employee, file, indent=4)
    print(f"JSON file is in: '{file_path3}'")

# CSV
employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 35, "Unemployed"],
             ["Sandy", 28, "Scientist"]]

file_path4 = "Harder Topics/files/output4.csv"

with open(file_path4, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"CSV file is in: '{file_path4}'")