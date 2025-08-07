def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def kilometers_to_miles(km):
    return km * 0.621371
def kilograms_to_pounds(kg):
    return kg * 2.20462
conversions = {
    "1": ("Celsius to Fahrenheit", celsius_to_fahrenheit, "°C", "°F"),
    "2": ("Kilometers to Miles", kilometers_to_miles, "km", "miles"),
    "3": ("Kilograms to Pounds", kilograms_to_pounds, "kg", "lbs")
}
def unit_converter():
    while True:
        print("\nUnit Converter Menu:")
        for key, value in conversions.items():
            print(f"{key}. {value[0]}")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "4":
            print("Thank you for using the unit converter!")
            break
        elif choice in conversions:
            try:
                amount = float(input(f"Enter value in {conversions[choice][2]}: "))
                result = conversions[choice][1](amount)
                print(f"{amount:.2f} {conversions[choice][2]} = {result:.2f} {conversions[choice][3]}")
            except ValueError:
                print("❌ Invalid number. Please enter a valid value.")
        else:
            print("❌ Invalid choice. Please select a valid option.")
unit_converter()
