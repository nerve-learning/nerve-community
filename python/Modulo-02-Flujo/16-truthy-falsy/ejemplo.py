# ejemplo.py

print("--- 1. Evaluando Texto Vacío ---")

# Simulamos que un usuario llenó un formulario en internet.
nombre_usuario = "Alejandro"
apellido_usuario = "" # Lo dejó en blanco

# En lugar de hacer 'if nombre_usuario != "":', usamos el atajo Truthy:
if nombre_usuario:
    print(f"Nombre ingresado: {nombre_usuario}")
else:
    print("Oye, no pusiste tu nombre.")

# Evaluamos el apellido. Al estar vacío "", es Falsy.
if apellido_usuario:
    print(f"Apellido ingresado: {apellido_usuario}")
else:
    print("El apellido es opcional, no pasa nada.")


print("\n--- 2. Evaluando Números ---")

# En un videojuego, verificamos si tienes pociones.
pociones = 0
monedas = 15

# Si tienes 0 pociones, 'pociones' actúa como False.
if pociones:
    print("Prepárate para curarte en la batalla.")
else:
    print("¡Cuidado! No tienes pociones, estás en peligro.")

# 15 es distinto de 0, así que es Truthy.
if monedas:
    print("Puedes pasar a la tienda a comprar cosas.")
else:
    print("Estás en la bancarrota.")


print("\n--- 3. La trampa del espacio en blanco ---")

comentario = " " # Hay un espacio entre las comillas

# ¿Un espacio en blanco es Truthy o Falsy?
# Para Python, un espacio es un carácter (algo físico), por lo tanto NO está vacío.
if comentario:
    print("¡El usuario dejó un comentario! (Aunque solo sea un espacio)")
else:
    print("El usuario no escribió absolutamente nada.")
