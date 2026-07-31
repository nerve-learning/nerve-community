# ==========================================
# Archivo: ejemplo.py
# Autor: Kaia / Alenia Studios
# Descripción: Comprendiendo la cremallera zip
# ==========================================

print("--- Base de Datos de Héroes ---")

# Tenemos dos listas separadas.
# Una con los nombres de los héroes y otra con sus superpoderes.
heroes = ["Flash", "Batman", "Superman"]
poderes = ["Super Velocidad", "Dinero", "Volar"]

print("Uniendo expedientes...")

# Usamos 'for' con DOS variables temporales: 'heroe' y 'poder'.
# Y usamos 'zip' para unir las dos listas.
for heroe, poder in zip(heroes, poderes):
    
    # En la primera vuelta:
    # heroe valdrá "Flash"
    # poder valdrá "Super Velocidad"
    
    print("Nombre:")
    print(heroe)
    print("Habilidad especial:")
    print(poder)
    print("--------------------")

print("--- Todos los expedientes revisados ---")
