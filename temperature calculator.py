def temp_convert(user_input):
    if user_input == "1":  # Convert from Celsius
        try:
            celsius_convert = float(input("Enter the temperature to be converted (in °C): "))
        except ValueError:
            print("Error: Please enter a valid number for temperature.")
            return

        # Choose the unit to convert to
        while True:
            try:
                convert_unit = int(input('''Please choose one of the following:
                1. Fahrenheit
                2. Kelvin\n'''))
                if convert_unit == 1:  # Convert to Fahrenheit
                    fahrenheit_converted = (celsius_convert * 9/5) + 32
                    print(f"{celsius_convert}°C is: {fahrenheit_converted}°F")
                    break
                elif convert_unit == 2:  # Convert to Kelvin
                    kelvin_converted = celsius_convert + 273.15
                    print(f"{celsius_convert}°C is: {kelvin_converted}K")
                    break
                else:
                    print("Error: Please choose a valid option (1 or 2).")
            except ValueError:
                print("Error: Please enter a valid number (1 or 2) for the unit selection.")

    elif user_input == "2":  # Convert from Fahrenheit
        try:
            fahrenheit_convert = float(input("Enter the temperature to be converted (in °F): "))
        except ValueError:
            print("Error: Please enter a valid number for temperature.")
            return

        # Choose the unit to convert to
        while True:
            try:
                convert_unit = int(input('''Please choose one of the following:
                1. Celsius
                2. Kelvin\n'''))
                if convert_unit == 1:  # Convert to Celsius
                    celsius_converted = (fahrenheit_convert - 32) * 5/9
                    print(f"{fahrenheit_convert}°F is: {celsius_converted}°C")
                    break
                elif convert_unit == 2:  # Convert to Kelvin
                    kelvin_converted = (fahrenheit_convert - 32) * 5/9 + 273.15
                    print(f"{fahrenheit_convert}°F is: {kelvin_converted}K")
                    break
                else:
                    print("Error: Please choose a valid option (1 or 2).")
            except ValueError:
                print("Error: Please enter a valid number (1 or 2) for the unit selection.")

    elif user_input == "3":  # Convert from Kelvin
        try:
            kelvin_convert = float(input("Enter the temperature to be converted (in K): "))
        except ValueError:
            print("Error: Please enter a valid number for temperature.")
            return

        # Choose the unit to convert to
        while True:
            try:
                convert_unit = int(input('''Please choose one of the following:
                1. Fahrenheit
                2. Celsius\n'''))
                if convert_unit == 1:  # Convert to Fahrenheit
                    fahrenheit_converted = (kelvin_convert - 273.15) * 9/5 + 32
                    print(f"{kelvin_convert}K is: {fahrenheit_converted}°F")
                    break
                elif convert_unit == 2:  # Convert to Celsius
                    celsius_converted = kelvin_convert - 273.15
                    print(f"{kelvin_convert}K is: {celsius_converted}°C")
                    break
                else:
                    print("Error: Please choose a valid option (1 or 2).")
            except ValueError:
                print("Error: Please enter a valid number (1 or 2) for the unit selection.")

    elif user_input == "4":
        print("Thank you for using the temperature converter.")
        exit()

    else:
        print("Error: Unknown input.")

# Main program loop
while True:
    print("\nTemperature Converter Menu:")
    print("1. Convert from Celsius")
    print("2. Convert from Fahrenheit")
    print("3. Convert from Kelvin")
    print("4. Exit")
    user_input = input("Please choose an option (1-4): ")
    temp_convert(user_input)
