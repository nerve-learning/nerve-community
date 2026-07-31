# ==========================================
# NIVEL 22: MÉTODOS DE LISTA - EJEMPLO PRÁCTICO
# ==========================================

print("--- 1. El inicio del viaje ---")
# Creamos nuestra lista inicial (nuestro autobús)
autobus = ["Conductor", "Señora mayor"]

print("Pasajeros actuales:")
print(autobus)


print("\n--- 2. Suben nuevos pasajeros (append) ---")
# Usamos el punto . para darle órdenes a la lista "autobus"
# .append() siempre pone el elemento al FINAL de la lista

autobus.append("Estudiante")
print("Se subió un estudiante. Pasajeros:")
print(autobus)

autobus.append("Músico")
print("Se subió un músico. Pasajeros:")
print(autobus)


print("\n--- 3. Bajan pasajeros (remove) ---")
# Usamos .remove() para decirle exactamente a quién queremos sacar
# La computadora buscará esa palabra exacta y la borrará.

autobus.remove("Señora mayor")
print("La señora mayor llegó a su destino. Pasajeros:")
print(autobus)


print("\n--- 4. Cuidado con las mayúsculas ---")
# Si intentamos borrar "estudiante" (en minúscula), nos dará error
# porque en la lista está como "Estudiante" (con E mayúscula).
# ¡La computadora es muy estricta con esto!

autobus.remove("Estudiante")
print("El estudiante se bajó en la escuela. Pasajeros:")
print(autobus)
