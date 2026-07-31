# ==========================================
# NIVEL 07: TEXTOS INTELIGENTES (F-STRINGS)
# ==========================================

print("--- Forma antigua (Sin f-strings) ---")

# Hasta ahora lo hacíamos así:
nombre = "Sam"
print("Hola")
print(nombre)
# O imprimía en varias líneas, o se veía muy torpe.

print("--- Forma nueva (Con f-strings) ---")

# Con la letra 'f' y las llaves '{}', lo hacemos en una sola línea.
print(f"Hola {nombre}, bienvenido de vuelta.")

print("--- Mezclando todo ---")

# Primero recolectamos los datos
usuario = input("¿Cuál es tu nombre? ")
estacion = input("¿A qué estación espacial viajas? ")
dias = 15
combustible = 99.5

# Y luego disparamos una sola oración que se lee fluidamente
print(f"Atención pasajero {usuario}. El vuelo hacia la {estacion} durará {dias} días. Nivel de combustible: {combustible}%.")
