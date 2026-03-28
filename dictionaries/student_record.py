# This program stores student data in a dictionary

student = {
    "name": input("Enter student name: "),
    "age": int(input("Enter student age: ")),
    "grade": float(input("Enter student grade: "))
}

print("\nStudent Data:")
for key, value in student.items():
    print(f"{key}: {value}")