# Alumno: Alberto Manana
total_segundos = int(input("Introduce una cantidad de segundos: "))

# La división entera y el resto permiten separar horas, minutos y segundos.
horas = total_segundos // 3600
segundos_restantes = total_segundos % 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(f"Tiempo convertido: {horas:02d} h, {minutos:02d} min y {segundos:02d} s")
