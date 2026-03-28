# This program reverses a list

numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

numbers.reverse()

print("Reversed list:", numbers)