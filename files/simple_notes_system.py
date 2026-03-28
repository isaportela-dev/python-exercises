# This program creates a simple notes system

while True:
    print("\n1 - Add note")
    print("2 - View notes")
    print("3 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        note = input("Write your note: ")
        
        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note saved!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                print("\n--- Notes ---")
                print(file.read())
        except FileNotFoundError:
            print("No notes found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")