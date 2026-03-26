# This program classifies a student's grade

grade = float(input("Enter your grade: "))

if grade >= 7:
    print("Approved")
elif grade >= 5:
    print("Recovery")
else:
    print("Failed")