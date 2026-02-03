# main.py

from length import meter_to_kilometer, kilometer_to_meter, centimeter_to_meter
from weight import kilogram_to_gram, gram_to_kilogram, kilogram_to_pound
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin
from storage import save_history, view_history

print("\n--- MEGA UNIT CONVERTER ---")
print("1. Length Conversion")
print("2. Weight Conversion")
print("3. Temperature Conversion")
print("4. View History")

choice = int(input("Choose category: "))

if choice == 1:
    print("\n1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Centimeter to Meter")
    opt = int(input("Choose option: "))
    val = float(input("Enter value: "))

    if opt == 1:
        res = meter_to_kilometer(val)
        text = f"{val} meter = {res} kilometer"
    elif opt == 2:
        res = kilometer_to_meter(val)
        text = f"{val} kilometer = {res} meter"
    else:
        res = centimeter_to_meter(val)
        text = f"{val} centimeter = {res} meter"

elif choice == 2:
    print("\n1. Kilogram to Gram")
    print("2. Gram to Kilogram")
    print("3. Kilogram to Pound")
    opt = int(input("Choose option: "))
    val = float(input("Enter value: "))

    if opt == 1:
        res = kilogram_to_gram(val)
        text = f"{val} kg = {res} g"
    elif opt == 2:
        res = gram_to_kilogram(val)
        text = f"{val} g = {res} kg"
    else:
        res = kilogram_to_pound(val)
        text = f"{val} kg = {res} pound"

elif choice == 3:
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    opt = int(input("Choose option: "))
    val = float(input("Enter value: "))

    if opt == 1:
        res = celsius_to_fahrenheit(val)
        text = f"{val} C = {res} F"
    elif opt == 2:
        res = fahrenheit_to_celsius(val)
        text = f"{val} F = {res} C"
    else:
        res = celsius_to_kelvin(val)
        text = f"{val} C = {res} K"

elif choice == 4:
    view_history()
    exit()

else:
    print("Invalid choice")
    exit()

print("\nResult:", text)
save_history(text)
