# --- 1. Preparando nuestras herramientas ---
import csv

print("--- Escribiendo una nueva tabla ---")

# Abrimos nuestro archivo en modo "w" (Escribir).
# Ponemos newline="" para evitar que aparezcan renglones vacíos extra en nuestra tabla.
with open("supermercado.csv", "w", newline="") as archivo_nuevo:
    
    # Creamos a nuestro "trabajador" que sabe cómo escribir formatos CSV
    escritor = csv.writer(archivo_nuevo)
    
    # Le decimos que escriba la primera fila (estos serán los encabezados de las columnas)
    # ¡Nota muy importante: Le pasamos una LISTA (con los corchetes)!
    escritor.writerow(["Producto", "Precio", "Cantidad"])
    
    # Ahora agregamos un par de filas de datos
    escritor.writerow(["Manzanas", 15, 3])
    escritor.writerow(["Leche", 20, 1])

print("¡Tabla de supermercado creada con éxito y guardada en tu computadora!\n")

# --- 2. Leyendo la tabla que acabamos de crear ---
print("--- Extrayendo datos de la tabla ---")

# Ahora abrimos el MISMO archivo pero en modo lectura "r"
with open("supermercado.csv", "r") as archivo_existente:
    
    # Creamos a nuestro "trabajador" que sabe cómo leer formatos CSV
    lector = csv.reader(archivo_existente)
    
    # El lector tiene todas las filas atrapadas adentro.
    # Usaremos un bucle 'for' para que nos dé una por una.
    for fila in lector:
        print("Acabo de leer esta fila:", fila)
        # Observa en tu terminal: cada fila ya no es texto simple,
        # ¡Python la convirtió en una Lista lista para que la usemos!

print("\n--- ¡Magia de las tablas completada! ---")
