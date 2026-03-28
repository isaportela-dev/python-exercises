# This function converts Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp = float(input("Enter temperature in Celsius: "))

result = celsius_to_fahrenheit(temp)

print("Temperature in Fahrenheit:", result)