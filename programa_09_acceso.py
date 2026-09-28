# Alumno: Alberto Manana
edad_usuario = int(input("Introduce tu edad: "))
respuesta_autorizacion = input("¿Tienes autorización? (si/no): ").strip().lower()
respuesta_identificacion = input("¿Tienes identificación? (si/no): ").strip().lower()

# El acceso completo exige cumplir simultáneamente las tres condiciones.
tiene_autorizacion = respuesta_autorizacion == "si"
tiene_identificacion = respuesta_identificacion == "si"
es_mayor_de_edad = edad_usuario >= 18
acceso_completo = es_mayor_de_edad and tiene_autorizacion and tiene_identificacion

print(f"Es mayor de edad: {es_mayor_de_edad}")
print(f"Tiene autorización: {tiene_autorizacion}")
print(f"Tiene identificación: {tiene_identificacion}")
print(f"Acceso completo permitido: {acceso_completo}")
