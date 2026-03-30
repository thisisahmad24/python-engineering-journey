# Build: File-Based Student Manager
import json

FILE_NAME = "students.json"


# Load data
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


# Save data
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file)


# Add student
def add_student(students):
    name = input("Enter name: ")
    age = input("Enter age: ")

    student = {"name": name, "age": age}
    students.append(student)

    save_students(students)
    print("✅ Student added successfully!")


# View students
def view_students(students):
    if not students:
        print("No students found.")
        return

    for s in students:
        print(f"Name: {s['name']}, Age: {s['age']}")


# Search student
def search_student(students):
    name = input("Enter name to search: ")

    found = False
    for s in students:
        if s["name"].lower() == name.lower():
            print(f"Found: {s}")
            found = True

    if not found:
        print("Student not found.")


# Main program
def main():
    students = load_students()

    while True:
        print("\n--- Student Manager ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


main()