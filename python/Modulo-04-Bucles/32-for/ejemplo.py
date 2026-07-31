# ==========================================
# Archivo: ejemplo.py
# Autor: Kaia / Alenia Studios
# Descripción: Comprendiendo el bucle for
# ==========================================

print("--- Revisión de Inventario ---")

# Creamos una lista usando corchetes y la guardamos en la variable 'inventario'.
inventario = ["brújula", "mapa", "antorcha", "cuerda"]

print("Vamos a revisar qué hay en tu bolsa de viaje:")

# Le decimos a la computadora:
# "Por cada (for) 'articulo' en (in) la lista 'inventario', entonces (:) haz esto:"
# Nota: 'articulo' es un nombre que inventamos nosotros. 
# Actúa como una caja temporal que guarda el objeto que estamos viendo en este momento.
for articulo in inventario:
    
    # Este bloque (por la indentación) se repetirá 4 veces, porque hay 4 cosas en la lista.
    print("Revisando objeto...")
    
    # Imprimimos lo que hay adentro de nuestra caja temporal 'articulo'.
    print(articulo)

print("--- Fin de la Revisión ---")

# Podemos usar un 'if' dentro de un 'for' si queremos!
print("Buscando si tenemos una antorcha...")

# Recorremos la misma lista otra vez.
for articulo in inventario:
    
    # Comprobamos (==) si el artículo actual es la antorcha.
    if articulo == "antorcha":
        # Esta línea tiene DOS niveles de indentación: 
        # uno por el 'for' y otro por el 'if'.
        print("¡Genial! Tenemos luz para la cueva.")

print("¡Todo listo para continuar!")
