# This program is a simple number guessing game

secret_number = 7

while True:
    guess = int(input("Guess the number: "))
    
    if guess == secret_number:
        print("You got it!")
        break
    else:
        print("Try again!")