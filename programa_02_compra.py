# Alumno: Alberto Manana
nombre_producto = input("Introduce el nombre del producto: ")
precio_producto = float(input("Introduce el precio del producto: "))
cantidad_productos = int(input("Introduce la cantidad de unidades: "))
porcentaje_iva = float(input("Introduce el IVA en formato decimal (por ejemplo, 0.21): "))

# El precio final se calcula separando el importe del impuesto.
subtotal = precio_producto * cantidad_productos
importe_iva = subtotal * porcentaje_iva
total_compra = subtotal + importe_iva

print(f"\nProducto: {nombre_producto}")
print(f"Precio unitario: {precio_producto:.2f} €")
print(f"Cantidad: {cantidad_productos}")
print(f"Subtotal: {subtotal:.2f} €")
print(f"IVA: {importe_iva:.2f} €")
print(f"Total de la compra: {total_compra:.2f} €")
