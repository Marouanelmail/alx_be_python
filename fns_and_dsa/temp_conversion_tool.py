#!/usr/bin/python3
# global FAHRENHEIT_TO_CELSIUS_FACTOR
# global CELSIUS_TO_FAHRENHEIT_FACTOR
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
temp = int(input("Enter the temperature to convert: "))

def convert_to_celsius(fahrenheit):
    # global CELSIUS_TO_FAHRENHEIT_FACTOR
    celisius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celisius
# def convert_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celisius):
    # global FAHRENHEIT_TO_CELSIUS_FACTOR
    fahrenheit = (celisius* CELSIUS_TO_FAHRENHEIT_FACTOR) +32
    return fahrenheit
# def convert_to_fahrenheit(celsius):
#     return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

cel_or_fahr = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
match cel_or_fahr:
    case "F":
        print(f"{temp}°F is {convert_to_celsius(temp)}°C")
    case "C":
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")