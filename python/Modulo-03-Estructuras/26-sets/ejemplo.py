# ==========================================
# NIVEL 26: SETS (CONJUNTOS) - EJEMPLO PRÁCTICO
# ==========================================

print("--- 1. Creando un Set ---")
# Usamos llaves { } pero SIN los dos puntos :
sabores_helado = {"Vainilla", "Chocolate", "Fresa"}

print("Los sabores disponibles son:")
print(sabores_helado)


print("\n--- 2. El destructor de clones ---")
# Vamos a intentar engañar al Set metiendo "Chocolate" muchas veces.
sabores_repetidos = {"Vainilla", "Chocolate", "Chocolate", "Chocolate", "Fresa"}

print("Intenté meter Chocolate tres veces, pero el Set dice:")
# ¡Solo mostrará un Chocolate!
print(sabores_repetidos)


print("\n--- 3. Añadiendo elementos al club (.add) ---")
# Para las listas usábamos .append()
# Para los Sets usamos .add() (que significa "añadir" en inglés)
sabores_helado.add("Menta")
print("Añadimos Menta:")
print(sabores_helado)

# Si intentamos añadir algo que ya existe, no pasa nada, no da error, solo lo ignora.
sabores_helado.add("Vainilla")
print("Intentamos añadir Vainilla de nuevo (ya estaba):")
print(sabores_helado)


print("\n--- 4. Quitando elementos (.remove) ---")
# .remove() funciona igual que en las listas
sabores_helado.remove("Fresa")
print("Se acabó la Fresa:")
print(sabores_helado)

# IMPORTANTE: Nota cómo al imprimir a veces el orden cambia.
# ¡Los Sets no garantizan que el orden se mantenga!
