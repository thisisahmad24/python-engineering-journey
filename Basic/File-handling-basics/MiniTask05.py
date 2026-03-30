# Build: File-Based Student Manager
import json
students = []
while True:
    name = input("Enter name: ")
    age = input("Enter age: ")

    student = {"name": name, "age": age}
    students.append(student)

    choice = input("Add more? (yes/no): ")
    if choice == "no":
        break
# Save to file
with open("students.json", "w") as file:
    json.dump(students, file)
print("Data saved successfully!")

#Retrieve From file
with open("students.json", "r") as file:
    data = json.load(file)
print(data)