# This program adds new content to an existing file

with open("example.txt", "a") as file:
    file.write("\nThis line was added later.")

print("Content appended successfully.")