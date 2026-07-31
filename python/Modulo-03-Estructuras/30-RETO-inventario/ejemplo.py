import copy

print("--- 1. Creando al Héroe ---")

# Tupla: Las coordenadas de inicio nunca cambian, nacimos ahí.
coordenadas_inicio = (10, 50)

# Diccionario: Las propiedades del héroe con etiquetas claras.
heroe = {
    "nombre": "Arthur",
    "clase": "Caballero",
    "nivel": 5,
    "oro": 150
}

# Lista: Los objetos en la mochila (el orden importa, el primero es el más accesible).
mochila = ["Espada de madera", "Poción de salud", "Antorcha"]

# Set: Lugares que ya visitó (no importa el orden, y no puedes descubrir el mismo lugar dos veces).
lugares_descubiertos = {"Bosque Oscuro", "Pueblo Inicial"}

print("El héroe", heroe["nombre"], "ha nacido en las coordenadas", coordenadas_inicio)

print("\n--- 2. Aventura y Cambios ---")

# El héroe encuentra oro y sube de nivel (actualizando diccionario)
heroe["oro"] = heroe["oro"] + 50
heroe["nivel"] = 6

# El héroe encuentra un escudo y lo guarda al final de la mochila (lista)
mochila.append("Escudo de hierro")

# El héroe usa la espada de madera y se rompe (borrando de lista)
mochila.remove("Espada de madera")

# El héroe descubre una cueva secreta (añadiendo a set)
lugares_descubiertos.add("Cueva del Dragón")
# Si intentamos añadir el pueblo otra vez, el Set simplemente lo ignorará:
lugares_descubiertos.add("Pueblo Inicial")

print("Nuevas estadísticas:", heroe)
print("Mochila actual:", mochila)
print("Lugares visitados:", lugares_descubiertos)


print("\n--- 3. El Multiverso (Clonación Profunda) ---")

# Creamos un universo paralelo guardando TODO en un diccionario maestro anidado.
partida_guardada = {
    "personaje": heroe,
    "inventario": mochila,
    "mapa": lugares_descubiertos
}

# Hacemos un clon profundo de la partida guardada para no dañar la original.
partida_clon = copy.deepcopy(partida_guardada)

# En el universo paralelo (clon), el héroe pierde todo su oro por una maldición.
partida_clon["personaje"]["oro"] = 0
partida_clon["inventario"].append("Maldición del Eco")

print("Oro en partida original:", partida_guardada["personaje"]["oro"])
print("Oro en partida clonada:", partida_clon["personaje"]["oro"])
# Como usamos deepcopy, arruinar el clon no afectó a nuestra partida original.
