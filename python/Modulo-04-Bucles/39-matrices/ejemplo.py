# ==========================================
# Archivo: ejemplo.py
# Autor: Kaia / Alenia Studios
# Descripción: Explorando una Matriz con bucles anidados
# ==========================================

print("--- Entrando a la Mazmorra ---")

# Creamos un mapa de 3 pasillos.
# Cada pasillo (lista) tiene 3 habitaciones.
mapa_mazmorra = [
    ["vacia", "vacia", "monstruo"],
    ["vacia", "pocion", "vacia"],
    ["trampa", "vacia", "salida"]
]

# El primer bucle (el de afuera) recorre los PASILLOS.
for pasillo in mapa_mazmorra:
    
    print("-> Explorando un nuevo pasillo...")
    
    # El segundo bucle (el de adentro) recorre las HABITACIONES de ese pasillo.
    for habitacion in pasillo:
        
        # Este código tiene doble indentación.
        print("Abrí una puerta y encontré:")
        print(habitacion)
        
        # Podemos meter condicionales aquí adentro (¡triple indentación!)
        if habitacion == "monstruo":
            print("¡A luchar!")

    # Cuando terminamos un pasillo completo, imprimimos un separador.
    # Nota que este print está alineado con el bucle interior,
    # así que se ejecuta después de revisar todas las puertas de un pasillo.
    print("Pasillo terminado.")
    print("------------------")

print("--- Has salido de la Mazmorra ---")
