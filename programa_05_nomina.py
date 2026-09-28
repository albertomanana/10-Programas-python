# Alumno: Alberto Manana
nombre_empleado = input("Introduce el nombre del empleado: ")
horas_trabajadas = float(input("Introduce las horas trabajadas: "))
precio_hora = float(input("Introduce el precio por hora: "))
porcentaje_retencion = float(input("Introduce la retención en formato decimal (por ejemplo, 0.15): "))

# La nómina resta la retención calculada sobre el salario bruto.
salario_bruto = horas_trabajadas * precio_hora
importe_retencion = salario_bruto * porcentaje_retencion
salario_neto = salario_bruto - importe_retencion

print(f"\nEmpleado: {nombre_empleado}")
print(f"Salario bruto: {salario_bruto:.2f} €")
print(f"Retención: {importe_retencion:.2f} €")
print(f"Salario neto: {salario_neto:.2f} €")
