# This program stores contacts in a dictionary

contacts = {}

while True:
    name = input("Enter contact name (or 'exit' to stop): ")
    
    if name == "exit":
        break
    
    phone = input("Enter phone number: ")
    
    contacts[name] = phone

print("\nContact List:")
for name, phone in contacts.items():
    print(f"{name}: {phone}")