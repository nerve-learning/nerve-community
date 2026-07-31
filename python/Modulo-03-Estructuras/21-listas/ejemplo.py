# ==========================================
# NIVEL 21: LISTAS - EJEMPLO PRÁCTICO
# ==========================================

print("--- 1. La caja de un solo espacio vs La caja organizadora ---")

# Hasta ahora, hacíamos esto (variables sueltas):
personaje_principal = "Héroe"
personaje_secundario = "Mago"
personaje_terciario = "Arquero"

# ¡Imagina hacer eso para 100 personajes!

# Ahora, usamos una LISTA (caja organizadora):
# Fíjate en los corchetes [ ] y las comas ,
equipo_rpg = ["Héroe", "Mago", "Arquero"]

print("Mi equipo es:")
print(equipo_rpg)


print("\n--- 2. Listas de números ---")
# También podemos hacer listas de números, sin comillas (porque son números)
edades_del_equipo = [25, 120, 34]

print("Edades de los miembros:")
print(edades_del_equipo)


print("\n--- 3. Una lista vacía ---")
# Podemos crear una lista que no tenga nada dentro todavía.
# Es como comprar una caja organizadora vacía para llenarla después.
mochila_vacia = []

print("Mi mochila al inicio de la aventura:")
print(mochila_vacia)


print("\n--- 4. Mezclando tipos de datos ---")
# Una lista puede tener textos, números y booleanos al mismo tiempo
ficha_de_personaje = ["Héroe", 25, 1.80, True]

print("Ficha completa del héroe (Nombre, Edad, Altura, ¿Está vivo?):")
print(ficha_de_personaje)
