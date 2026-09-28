# Alumno: Alberto Manana
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
altura_metros = float(input("Introduce tu altura en metros: "))
ciudad = input("Introduce tu ciudad: ")
experiencia_programando = input("Describe tu experiencia programando: ")

# Se muestran todos los datos introducidos en una ficha legible.
print(f"\nFicha de {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura_metros:.2f} m")
print(f"Ciudad: {ciudad}")
print(f"Experiencia: {experiencia_programando}")
