# Importamos el módulo que nos permite hablar con Internet
# Piensa en 'requests' como nuestro teléfono celular.
import requests

print("--- 1. Preparando la llamada ---")
# La URL es la dirección exacta a la que vamos a llamar.
# En este caso, llamamos a la PokéAPI, preguntando por 'pikachu'.
direccion_pikachu = "https://pokeapi.co/api/v2/pokemon/pikachu"

print(f"Vamos a llamar a: {direccion_pikachu}")


print("\n--- 2. Haciendo la petición a Internet ---")
# requests.get() es la acción de marcar el número y esperar a que contesten.
# Lo que el servidor nos responda, lo guardaremos en la variable 'respuesta'.
# IMPORTANTE: El programa se quedará pausado aquí unos milisegundos 
# mientras la señal viaja por Internet y regresa.
respuesta = requests.get(direccion_pikachu)

# status_code nos dice cómo nos fue en la llamada. 
# El número 200 significa "OK, todo perfecto". (Como cuando te contestan "¡Hola, dime!")
# El número 404 significa "No encontrado". (Como cuando te dicen "El número marcado no existe")
print("Estado de la respuesta:", respuesta.status_code)


print("\n--- 3. Traduciendo los datos recibidos ---")
# La respuesta viene en un formato llamado JSON (texto puro).
# Para poder buscar datos fácilmente, usamos .json() para 
# traducirlo a un Diccionario de Python.
datos_pokemon = respuesta.json()

# Ahora 'datos_pokemon' es un diccionario gigante con toda la info de Pikachu.
# Como sabemos usar diccionarios, podemos acceder a sus llaves ("keys"):
print("Traducción completada con éxito.")


print("\n--- 4. Explorando la información de nuestro Diccionario ---")
# Usamos corchetes [] y el nombre de la llave para sacar el valor.
nombre = datos_pokemon["name"]
altura = datos_pokemon["height"]
peso = datos_pokemon["weight"]

print(f"Nombre del Pokémon: {nombre.capitalize()}")
print(f"Altura: {altura} decímetros")
print(f"Peso: {peso} hectogramos")

print("\n--- ¡Misión Cumplida! ---")
print("Nuestro código acaba de leer información viva desde otra computadora en el mundo.")
