# This program checks if a word is a palindrome

text = input("Enter a word: ").lower()

if text == text[::-1]:
    print("It is a palindrome")
else:
    print("Not a palindrome")