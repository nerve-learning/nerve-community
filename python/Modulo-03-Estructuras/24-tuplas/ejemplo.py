# ==========================================
# NIVEL 24: TUPLAS - EJEMPLO PRÁCTICO
# ==========================================

print("--- 1. Creando una Tupla (Caja Fuerte) ---")
# Usamos paréntesis ( ) en lugar de corchetes [ ]
coordenadas_casa = (19.43, -99.13)

print("Las coordenadas de mi casa son:")
print(coordenadas_casa)


print("\n--- 2. Leyendo los datos de la tupla ---")
# Para LEER, usamos los corchetes de índice [0], igual que en las listas.
# ¡Los paréntesis solo son para crearla!
latitud = coordenadas_casa[0]
longitud = coordenadas_casa[1]

print("Latitud exacta:")
print(latitud)
print("Longitud exacta:")
print(longitud)


print("\n--- 3. La prueba del candado ---")
print("¿Qué pasa si intentamos añadir algo?")
print("(Esto está comentado para que no explote el programa)")

# Si le quitamos el símbolo '#' a la siguiente línea, el programa fallará:
# coordenadas_casa.append(10.0)

print("Si lo intentas, Python dirá: AttributeError (no se puede agregar).")


print("\n--- 4. Listas vs Tuplas juntas ---")
# Podemos tener listas que guardan tuplas adentro. 
# Piensa en una caja de cartón que adentro tiene pequeñas cajitas fuertes.
ruta_gps = [
    (0.0, 0.0),   # Inicio (tupla)
    (5.5, 2.1),   # Medio (tupla)
    (10.0, 9.9)   # Fin (tupla)
]

print("Mi ruta GPS tiene varios puntos sellados:")
print(ruta_gps)
