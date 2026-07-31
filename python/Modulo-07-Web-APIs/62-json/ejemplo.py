# Importamos la herramienta oficial de Python para traducir JSON
import json

print("--- 1. Recibiendo un paquete de Internet ---")
# Imagina que este texto llegó a través de la red.
# Fíjate que está envuelto en comillas simples por fuera ('') 
# porque adentro usa comillas dobles ("") obligatorias de JSON.
paquete_recibido = '{"personaje": "Link", "juego": "Ocarina of Time", "corazones": 3}'

print(f"Acabamos de recibir este texto: {paquete_recibido}")
print("Tipo de dato recibido:", type(paquete_recibido)) # Nos dirá que es 'str' (String/Texto)


print("\n--- 2. Desempacando el paquete (Texto -> Diccionario) ---")
# json.loads() significa "Load String" (Cargar Texto).
# Toma el texto muerto y le da vida como un Diccionario de Python.
inventario = json.loads(paquete_recibido)

print("Tipo de dato después de desempacar:", type(inventario)) # Nos dirá que es 'dict'

# ¡Como es un diccionario, ahora podemos acceder a sus partes fácilmente!
print(f"El héroe es {inventario['personaje']} y tiene {inventario['corazones']} corazones.")


print("\n--- 3. Empacando un nuevo paquete (Diccionario -> Texto) ---")
# Hemos terminado nuestra misión y queremos avisar al servidor.
# Primero, armamos nuestro diccionario en Python con total libertad.
mi_mensaje = {
    "usuario": "Link",
    "accion": "Derrotar Jefe",
    "mision_cumplida": True # Nota que en Python usamos True en mayúscula
}

# json.dumps() significa "Dump String" (Volcar a Texto).
# Aplasta el diccionario para convertirlo en formato universal.
paquete_para_enviar = json.dumps(mi_mensaje)

print("Paquete empacado y listo para viajar por la red:")
print(paquete_para_enviar)
print("Tipo de dato ahora:", type(paquete_para_enviar)) # Vuelve a ser 'str'

print("\n--- ¡Operación JSON Exitosa! ---")
print("Ya sabes hablar el idioma universal de las computadoras.")
