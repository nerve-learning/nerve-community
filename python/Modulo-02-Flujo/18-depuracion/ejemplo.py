# ejemplo.py

print("--- 1. El Misterio del Descuento Perdido ---")
# Contexto: Un cliente compró 3 artículos de 40 dólares. 
# Si gasta más de 100 dólares, debería tener descuento.

precio_articulo = 40
cantidad = 3

# Calculamos el total
total = precio_articulo + cantidad  # ¡Uups! Usé el símbolo de suma (+) en vez de multiplicar (*)

# Aquí está el problema: el programador dice "Debería entrar al if porque 40 * 3 = 120".
# Pero cuando corre el código...

# --- INICIA ZONA DE DEPURACIÓN ---
# Como no funciona, encendemos la linterna con 'print()'
print("DEBUG - El precio del artículo es:", precio_articulo)
print("DEBUG - La cantidad es:", cantidad)
print("DEBUG - El total calculado es:", total) 
# ¡Ahí veremos que total es 43, no 120! ¡Encontramos el bug!
# --- TERMINA ZONA DE DEPURACIÓN ---

if total > 100:
    print("¡Felicidades! Tienes un descuento.")
else:
    print("No alcanzas el descuento. Sigue comprando.")


print("\n--- 2. Rastreando los pasos de Python ---")
# A veces no sabemos por qué camino se fue el código. Ponemos "letreros" en el camino.

clima = "lluvia"
temperatura = 15

# Colocamos un 'print' de diagnóstico para confirmar los valores iniciales.
print("DEBUG - Estado inicial -> clima:", clima, "/ temp:", temperatura)

if clima == "soleado":
    print("DEBUG - Camino A (soleado)")
    if temperatura > 25:
        print("Vamos a la playa.")
    else:
        print("Vamos al parque.")
elif clima == "lluvia":
    print("DEBUG - Camino B (lluvia)")
    if temperatura < 10:
        print("DEBUG - Camino B.1 (frío)")
        print("Quédate en cama con un chocolate.")
    else:
        print("DEBUG - Camino B.2 (no tan frío)")
        print("Lleva paraguas.")
else:
    print("DEBUG - Camino C (otro)")
    print("Mira por la ventana.")
