# Alumno: Alberto Manana
entradas_disponibles = int(input("Introduce el número de entradas disponibles: "))
numero_grupos = int(input("Introduce el número de grupos: "))

# La división entera reparte las entradas y el resto indica las sobrantes.
entradas_por_grupo = entradas_disponibles // numero_grupos
entradas_sobrantes = entradas_disponibles % numero_grupos

print(f"Entradas para cada grupo: {entradas_por_grupo}")
print(f"Entradas sobrantes: {entradas_sobrantes}")
