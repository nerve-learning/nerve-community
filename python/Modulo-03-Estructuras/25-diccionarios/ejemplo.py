# ==========================================
# NIVEL 25: DICCIONARIOS - EJEMPLO PRÁCTICO
# ==========================================

print("--- 1. Creando nuestro primer Diccionario ---")
# Usamos llaves { } y parejas separadas por dos puntos :
perfil_jugador = {
    "nombre": "Arthur",
    "nivel": 42,
    "esta_vivo": True
}

print("El perfil completo del jugador es:")
print(perfil_jugador)


print("\n--- 2. Buscando datos específicos ---")
# En vez de usar números [0], usamos el nombre de la clave ["nombre"]
nombre_actual = perfil_jugador["nombre"]
nivel_actual = perfil_jugador["nivel"]

print("Buscando en los registros...")
print("El jugador se llama:")
print(nombre_actual)
print("Su nivel de poder es:")
print(nivel_actual)


print("\n--- 3. Modificando un valor ---")
# Si Arthur sube de nivel, buscamos la clave y le asignamos un nuevo valor
print("¡Arthur ha ganado experiencia!")

perfil_jugador["nivel"] = 43

print("El nuevo nivel de Arthur es:")
print(perfil_jugador["nivel"])


print("\n--- 4. Agregando una nueva pareja ---")
# Si la clave NO existe y le asignamos un valor, Python la crea automáticamente
perfil_jugador["arma"] = "Espada Mágica"

print("Se ha añadido un arma al perfil:")
print(perfil_jugador)
