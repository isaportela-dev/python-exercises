# This program writes text to a file

with open("example.txt", "w") as file:
    file.write("Hello, this is my first file in Python!\n")
    file.write("Learning file handling is important.")

print("File created and written successfully.")