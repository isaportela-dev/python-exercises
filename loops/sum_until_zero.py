# This program keeps asking for numbers until the user enters 0

total = 0

while True:
    number = float(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break
    
    total += number

print("Total sum:", total)