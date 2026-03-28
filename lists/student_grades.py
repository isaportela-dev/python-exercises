# This program stores student grades and calculates the average

grades = []

n = int(input("How many grades do you want to enter? "))

for i in range(n):
    grade = float(input(f"Enter grade {i+1}: "))
    grades.append(grade)

average = sum(grades) / len(grades)

print("Grades:", grades)
print("Average:", average)