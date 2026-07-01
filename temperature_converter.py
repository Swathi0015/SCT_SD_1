def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def celsius_to_kelvin(c):
    return c + 273.15


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32


def display_menu():
    print("\n========== Temperature Converter ==========")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    print("4. Exit")


while True:
    display_menu()

    try:
        choice = int(input("Choose the input temperature scale (1-4): "))

        if choice == 4:
            print("Thank you for using Temperature Converter!")
            break

        if choice not in [1, 2, 3]:
            print("Invalid choice! Please select a valid option.")
            continue

        temperature = float(input("Enter the temperature value: "))

        print("\nConverted Temperatures:")

        if choice == 1:
            print(f"Fahrenheit : {celsius_to_fahrenheit(temperature):.2f} °F")
            print(f"Kelvin     : {celsius_to_kelvin(temperature):.2f} K")

        elif choice == 2:
            print(f"Celsius    : {fahrenheit_to_celsius(temperature):.2f} °C")
            print(f"Kelvin     : {fahrenheit_to_kelvin(temperature):.2f} K")

        elif choice == 3:
            if temperature < 0:
                print("Kelvin cannot be less than 0.")
                continue

            print(f"Celsius    : {kelvin_to_celsius(temperature):.2f} °C")
            print(f"Fahrenheit : {kelvin_to_fahrenheit(temperature):.2f} °F")

    except ValueError:
        print("Please enter a valid numeric value.")