# ==========================================
# NIVEL 28: MUTABILIDAD - EJEMPLO PRÁCTICO
# ==========================================

print("--- 1. Inmutables: Cada quien su caja ---")
oro_jugador_1 = 100
oro_jugador_2 = oro_jugador_1  # Parece una copia

print("Jugador 1 encuentra un tesoro (+50)")
oro_jugador_1 = oro_jugador_1 + 50

print("Oro Jugador 1:", oro_jugador_1)
print("Oro Jugador 2:", oro_jugador_2) # Sigue en 100, no se afectó.


print("\n--- 2. Mutables: Compartiendo la misma caja ---")
inventario_1 = ["Espada", "Escudo"]
inventario_2 = inventario_1  # ¡ATENCIÓN! No es una copia, es la MISMA caja.

print("Jugador 2 encuentra una 'Poción' y la guarda en su inventario.")
inventario_2.append("Poción")

print("¿Qué tiene el Jugador 1 en su inventario?")
print(inventario_1)
# ¡Sorpresa! El inventario 1 también tiene la poción.
# ¡Están compartiendo la misma mochila!


print("\n--- 3. ¿Cómo hago una copia real entonces? ---")
# Para hacer un "clon" real de una lista, usamos el rebanado o slicing [:]
# Dejando todo vacío antes y después de los dos puntos :, 
# le decimos "corta la lista desde el inicio al final y pon el resultado en una caja NUEVA".

lista_original = ["A", "B", "C"]
copia_real = lista_original[:]  # <- ¡El truco mágico!

lista_original.append("D")

print("Lista Original:", lista_original)
print("Copia Real:", copia_real) # Esta sí se mantuvo intacta.
