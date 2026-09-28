# Alumno: Alberto Manana
primer_numero = int(input("Introduce el primer número entero: "))
segundo_numero = int(input("Introduce el segundo número entero: "))

# Se calculan las operaciones básicas y se evita dividir entre cero.
suma = primer_numero + segundo_numero
resta = primer_numero - segundo_numero
multiplicacion = primer_numero * segundo_numero
potencia = primer_numero ** segundo_numero

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"Potencia: {potencia}")
if segundo_numero != 0:
    print(f"División real: {primer_numero / segundo_numero:.2f}")
    print(f"División entera: {primer_numero // segundo_numero}")
    print(f"Resto: {primer_numero % segundo_numero}")
else:
    print("División real: no disponible (el divisor es cero)")
    print("División entera y resto: no disponibles (el divisor es cero)")
