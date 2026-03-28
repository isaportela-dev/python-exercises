# This program simulates a simple inventory system

inventory = {}

n = int(input("How many products? "))

for i in range(n):
    name = input("Product name: ")
    quantity = int(input("Quantity: "))
    
    inventory[name] = quantity

print("\nInventory:")
for product, qty in inventory.items():
    print(f"{product}: {qty}")