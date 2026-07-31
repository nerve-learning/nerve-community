# ==========================================
# NIVEL 23: ÍNDICES Y SLICING - EJEMPLO PRÁCTICO
# ==========================================

print("--- 1. El podio de la carrera ---")
# Aquí están los corredores que llegaron a la meta, en orden.
corredores = ["Flash", "Sonic", "Quicksilver", "Dash"]

print("Todos los corredores:")
print(corredores)


print("\n--- 2. Entregando la medalla de oro ---")
# El primer lugar está en la posición CERO [0]
medalla_oro = corredores[0]

print("La medalla de oro es para:")
print(medalla_oro)

print("La medalla de plata (posición 1) es para:")
print(corredores[1])


print("\n--- 3. Los mejores 3 (Slicing) ---")
# Queremos un "pedazo" de la lista con el top 3.
# Empezamos en 0 y terminamos ANTES del 3 (es decir, posiciones 0, 1 y 2).
# Usamos los dos puntos :
top_tres = corredores[0:3]

print("Los corredores en el podio son:")
print(top_tres)


print("\n--- 4. Atajos del Slicing ---")
# Si empiezas desde el principio, puedes dejar el espacio antes del : vacío.
# [:2] es lo mismo que decir "desde el inicio hasta antes del 2".
# Si quieres desde una posición hasta el final, dejas el segundo vacío.
# [2:] es lo mismo que decir "desde el 2 hasta el final".

los_ultimos = corredores[2:]
print("Los que no ganaron medalla:")
print(los_ultimos)
