# This program calculates discount based on purchase value

price = float(input("Enter the product price: "))

if price >= 100:
    discount = price * 0.10
    final_price = price - discount
    print("10% discount applied")
    print("Final price:", final_price)
else:
    print("No discount applied")
    print("Final price:", price)