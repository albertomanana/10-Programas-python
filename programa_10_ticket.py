# Alumno: Alberto Manana
nombre_cliente = input("Introduce el nombre del cliente: ")
nombre_producto = input("Introduce el nombre del producto: ")
precio_unitario = float(input("Introduce el precio unitario: "))
cantidad_productos = int(input("Introduce la cantidad: "))
porcentaje_descuento = float(input("Introduce el descuento en formato decimal (por ejemplo, 0.10): "))
porcentaje_iva = float(input("Introduce el IVA en formato decimal (por ejemplo, 0.21): "))

# Primero se descuenta el descuento y después se aplica el IVA al importe resultante.
subtotal = precio_unitario * cantidad_productos
importe_descuento = subtotal * porcentaje_descuento
total_con_descuento = subtotal - importe_descuento
importe_iva = total_con_descuento * porcentaje_iva
total_ticket = total_con_descuento + importe_iva

print("\n--- TICKET ---")
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {nombre_producto}")
print(f"Cantidad: {cantidad_productos}")
print(f"Subtotal: {subtotal:.2f} €")
print(f"Descuento: {importe_descuento:.2f} €")
print(f"IVA: {importe_iva:.2f} €")
print(f"Total: {total_ticket:.2f} €")
