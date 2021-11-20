def celsius_fahrenheit(celcius):
    print(f'{celcius}°C = {celcius * 9 / 5 + 32}°F')


def fahrenheit_celsius(fahrenheit):
    print(f'{fahrenheit}°F = {(fahrenheit - 32) * 5 / 9}°C')


celcius = float(input("Ingrese la temperatura en °C: "))
celsius_fahrenheit(celcius)

fahrenheit = float(input("Ingrese la temperatura en °F: "))
fahrenheit_celsius(fahrenheit)
