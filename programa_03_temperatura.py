# Alumno: Alberto Manana
temperatura_celsius = float(input("Introduce la temperatura en Celsius: "))

# Se aplican las fórmulas de conversión a las dos escalas solicitadas.
temperatura_fahrenheit = temperatura_celsius * 9 / 5 + 32
temperatura_kelvin = temperatura_celsius + 273.15

print(f"Temperatura en Fahrenheit: {temperatura_fahrenheit:.2f} °F")
print(f"Temperatura en Kelvin: {temperatura_kelvin:.2f} K")
