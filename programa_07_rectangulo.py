# Alumno: Alberto Manana
base_rectangulo = float(input("Introduce la base del rectángulo: "))
altura_rectangulo = float(input("Introduce la altura del rectángulo: "))

# Con la base y la altura se obtienen sus tres medidas principales.
area_rectangulo = base_rectangulo * altura_rectangulo
perimetro_rectangulo = 2 * (base_rectangulo + altura_rectangulo)
diagonal_rectangulo = (base_rectangulo ** 2 + altura_rectangulo ** 2) ** 0.5

print(f"Área del rectángulo: {area_rectangulo:.2f}")
print(f"Perímetro del rectángulo: {perimetro_rectangulo:.2f}")
print(f"Diagonal del rectángulo: {diagonal_rectangulo:.2f}")
