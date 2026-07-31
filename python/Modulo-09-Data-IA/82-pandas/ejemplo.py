# Traemos a nuestro experto en tablas y le llamamos "pd"
import pandas as pd

print("--- 1. Preparando los ingredientes (El Diccionario) ---")
# Creamos un diccionario normal. 
# Las llaves son los títulos de las columnas.
# Las listas son los datos que irán hacia abajo en cada fila.
datos_empleados = {
    "Nombre": ["Laura", "Marcos", "Sofia"],
    "Puesto": ["Gerente", "Vendedor", "Cajera"],
    "Sueldo": [5000, 2000, 1500]
}
print("Diccionario normal creado (no es muy fácil de leer para humanos).")


print("\n--- 2. Cocinando la Tabla (El DataFrame) ---")
# Convertimos el diccionario en una tabla profesional
# Recuerda: D y F con mayúsculas
tabla_empleados = pd.DataFrame(datos_empleados)

# Al imprimir la tabla, Pandas la dibuja mágicamente con números de fila (0, 1, 2...)
print(tabla_empleados)


print("\n--- 3. Extrayendo solo una columna ---")
# Si solo queremos ver la columna de los sueldos, la llamamos por su llave ("Sueldo")
lista_sueldos = tabla_empleados["Sueldo"]
print("Solo los sueldos:")
print(lista_sueldos)
