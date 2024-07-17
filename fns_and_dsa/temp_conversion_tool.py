#!/usr/bin/python3
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)
temp = int(input("Enter the temperature to convert: "))

def convert_to_celsius(fahrenheit):
    celisius = (fahrenheit * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return celisius

def convert_to_fahrenheit(celisius):
    fahrenheit = celisius - 32
    result = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    return result

cel_or_fahr = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
match cel_or_fahr:
    case "F":
        print(f"{temp}°F is {convert_to_fahrenheit(temp)}°C")
    case "C":
        print(f"{temp}°C is {convert_to_celsius(temp)}°F")