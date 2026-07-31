# ejemplo.py

print("--- 1. El Cajero del Cine (if / else) ---")

edad_cliente = 15

# Evaluamos la primera condición (Plan A)
if edad_cliente >= 18:
    print("Puedes ver la película de terror.")
# Si la condición de arriba fue False (15 no es mayor a 18), saltamos al 'else'
else:
    print("Eres menor de edad. Ve a ver la película animada.")


print("\n--- 2. El Semáforo Inteligente (if / elif / else) ---")

color_semaforo = "amarillo"

# Plan A
if color_semaforo == "verde":
    print("Puedes avanzar 🟢")

# Plan B (Solo se evalúa si el Plan A falló)
elif color_semaforo == "amarillo":
    print("Ve frenando con precaución 🟡")

# Plan C (Solo se evalúa si el Plan A y Plan B fallaron)
elif color_semaforo == "rojo":
    print("¡ALTO TOTAL! 🔴")

# Plan Z de seguridad (Si no fue verde, ni amarillo, ni rojo)
else:
    print("El semáforo está roto, cruza con mucho cuidado. ❓")


print("\n--- 3. La trampa del código en cascada ---")
# Solo un bloque (el primero que sea True) se ejecuta. Los demás se ignoran.

dinero_en_bolsillo = 100

if dinero_en_bolsillo >= 10:
    print("Me alcanza para un chicle.")
elif dinero_en_bolsillo >= 50:
    print("Me alcanza para una hamburguesa.")
else:
    print("No compro nada.")

# OJO AQUÍ: Aunque 100 es mayor que 50 (la segunda regla también es cierta), 
# Python imprimirá "Me alcanza para un chicle" y terminará el proceso ahí mismo, 
# porque fue el primer 'True' que encontró de arriba hacia abajo.
