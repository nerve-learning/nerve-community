import pandas as pd

print("--- 1. El Desastre del Mundo Real ---")
# Usamos 'None' para representar que nos faltan datos
datos_sucios = {
    "Cliente": ["Ana", "Beto", "Carlos", "Diana"],
    "Edad": [25, None, 22, 30],       # ¡A Beto le falta la edad!
    "Compras": [5, 2, None, 10]       # ¡A Carlos le faltan las compras!
}

# Pandas convertirá los 'None' en 'NaN' (Not a Number)
tabla = pd.DataFrame(datos_sucios)
print("Nuestra tabla envenenada con NaN:")
print(tabla)


print("\n--- 2. Solución Drástica: Borrar los defectuosos ---")
# .dropna() elimina cualquier fila que tenga al menos un NaN
# Recuerda: SIEMPRE guardar el resultado en una variable
tabla_estricta = tabla.dropna()

print("Sobrevivieron solo los que tenían todos sus datos:")
print(tabla_estricta)


print("\n--- 3. Solución Amable: Rellenar los huecos ---")
# .fillna(0) buscará todos los NaN en la tabla y pondrá un 0
tabla_amable = tabla.fillna(0)

print("Nadie fue eliminado, pero los huecos ahora son ceros:")
print(tabla_amable)
