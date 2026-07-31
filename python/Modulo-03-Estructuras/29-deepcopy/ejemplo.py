# ==========================================
# IMPORTANTE: Los imports siempre van hasta arriba
# ==========================================
# Le decimos a Python: "Trae la caja de herramientas de copiado"
import copy

print("--- 1. El Problema del Clon Superficial [:] ---")

# Tenemos una mochila. Adentro tiene un termo (texto) y una cartuchera (lista interna).
mochila_original = ["Termo de agua", ["Lápiz", "Borrador"]]

# Intentamos clonar usando el truco de rebanar que ya sabíamos
mochila_clon_malo = mochila_original[:]

# Modificamos la cartuchera (la lista interna) en el clon malo.
# Entramos a la posición 1 (la cartuchera) y le agregamos un sacapuntas.
mochila_clon_malo[1].append("Sacapuntas")

print("Mochila ORIGINAL:", mochila_original)
print("Mochila CLON MALO:", mochila_clon_malo)
# ¡Oh no! El sacapuntas apareció en la original también. 
# El [:] copió la mochila grande, pero usó la MISMA cartuchera para ambas.


print("\n--- 2. La Solución: deepcopy ---")

# Tenemos una nueva mochila original (la reiniciamos)
mochila_nueva_original = ["Termo de agua", ["Lápiz", "Borrador"]]

# Usamos nuestra nueva herramienta para un clon profundo, real y total
mochila_clon_perfecto = copy.deepcopy(mochila_nueva_original)

# Modificamos la cartuchera (lista interna) en el clon perfecto
mochila_clon_perfecto[1].append("Regla")

print("Nueva Mochila ORIGINAL:", mochila_nueva_original)
print("Mochila CLON PERFECTO:", mochila_clon_perfecto)
# ¡Éxito! La regla SOLO está en el clon perfecto. 
# deepcopy creó una mochila nueva Y una cartuchera totalmente nueva adentro.
