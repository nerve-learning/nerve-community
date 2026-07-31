# ==========================================
# Archivo: ejemplo.py
# Autor: Kaia / Alenia Studios
# Descripción: Comprendiendo la fábrica range
# ==========================================

print("--- Rutina de Entrenamiento ---")
print("El atleta va a hacer 5 flexiones.")

# Usamos 'for' combinado con 'range(5)'.
# 'repeticion' es nuestra variable temporal que irá guardando los números: 0, 1, 2, 3, 4.
for repeticion in range(5):
    
    # Este código se repetirá 5 veces.
    print("El atleta hace una flexión...")
    
    # Imprimimos el número de la repetición que nos dio la máquina 'range'.
    # ¡Ojo! Imprimirá desde el 0 hasta el 4.
    print(repeticion)

print("--- Fin del Entrenamiento ---")

print("El atleta está descansando...")

# Podemos combinar texto y la variable temporal si queremos ver algo más claro.
print("Vamos a contar 3 segundos de descanso:")

for segundo in range(3):
    print("Segundo transcurrido:")
    print(segundo)

print("¡Atleta recuperado!")
