from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin

def main():
    print("Temperature Conversion Program")
    print("Choose conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {celsius_to_fahrenheit.convert(celsius):.2f}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_celsius.convert(fahrenheit):.2f}°C")
    elif choice == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {celsius_to_kelvin.convert(celsius):.2f}K")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
