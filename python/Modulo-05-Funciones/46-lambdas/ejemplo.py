print("--- 1. Cara a Cara: def vs lambda ---")

# Contrato formal (def)
def duplicar_formal(numero):
    return numero * 2

# Post-it rápido (lambda)
# Sintaxis: variable = lambda ingredientes : lo_que_devuelve
duplicar_rapido = lambda numero : numero * 2

print("Con def:", duplicar_formal(5))
print("Con lambda:", duplicar_rapido(5))
# ¡Ambas hacen exactamente lo mismo!


print("\n--- 2. Múltiples ingredientes en una Lambda ---")

# Queremos calcular el precio con un descuento
# Ingredientes: precio, descuento. Resultado: precio - descuento
aplicar_descuento = lambda precio, descuento : precio - descuento

precio_zapatos = aplicar_descuento(100, 20)
print("Tus zapatos con descuento cuestan:", precio_zapatos)


print("\n--- 3. Lambdas con texto ---")

# Las lambdas no son solo para matemáticas. También pueden unir textos.
# Ingredientes: nombre, apellido. Resultado: Unirlos con un espacio en medio.
crear_nombre_completo = lambda nombre, apellido : nombre + " " + apellido

jugador = crear_nombre_completo("Arthur", "Pendragon")
print("Bienvenido al juego,", jugador)


print("\n--- 4. Un error común para evitar ---")
# Si intentas hacer esto:
# lambda x : x = x + 1
# Python explotará. Las lambdas no están hechas para modificar variables (asignaciones con =).
# Solo están hechas para producir un resultado directo:
# lambda x : x + 1  (¡Así es correcto!)
