# ==========================================
# Archivo: ejemplo.py
# Autor: Kaia / Alenia Studios
# Descripción: Comprendiendo las List Comprehensions
# ==========================================

print("--- La Forja del Elfo ---")

# Tenemos el inventario de armas viejas y oxidadas.
armas_oxidadas = ["espada", "hacha", "daga"]

print("Armas en el taller:")
print(armas_oxidadas)

print("--- Aplicando magia élfica ---")

# Vamos a crear una NUEVA lista usando la máquina clonadora.
# Fórmula: [ACCION para cada ELEMENTO en LISTA_VIEJA]
# La ACCION es: agarrar el 'arma', sumarle (+) un espacio, y la palabra "mágica" o "mágico".
# El MOTOR es: for arma in armas_oxidadas

armas_mejoradas = [arma + " mágica" for arma in armas_oxidadas]

# ¡Eso es todo! En una sola línea hemos recorrido la lista vieja,
# modificado cada palabra, y guardado el resultado en una lista nueva.

print("¡Las armas han sido mejoradas de golpe!")
print("Inventario nuevo:")
print(armas_mejoradas)

print("--- Forja Cerrada ---")
