# This program finds the largest number in a list

numbers = []

for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

largest = max(numbers)

print("Largest number:", largest)