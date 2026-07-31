# --- 1. Preparando nuestro equipo de exploración ---
# La palabra 'import' le dice a Python: "Por favor, trae la caja de herramientas..."
# 'os' es la caja de herramientas del Sistema Operativo.
import os

print("--- ¿Dónde estoy parado? ---")

# Usamos el punto '.' para sacar la herramienta 'getcwd' de la caja 'os'.
# Esta herramienta pregunta: "¿Cuál es mi ruta actual?"
# Como es una acción, ponemos los paréntesis () al final.
# Luego, el símbolo '=' guarda la respuesta en nuestra variable.
mi_ubicacion = os.getcwd()

print("Python dice que ahora mismo estamos en esta dirección:")
print(mi_ubicacion)


print("\n--- ¿Qué hay a mi alrededor? ---")

# Otra herramienta de la caja 'os' es 'listdir' (List Directory = Listar Directorio).
# A esta herramienta le damos a comer nuestra ubicación entre los paréntesis,
# y nos devuelve una LISTA con los nombres de todo lo que hay ahí.
cosas_a_mi_alrededor = os.listdir(mi_ubicacion)

# ¡Tú ya sabes cómo funcionan las listas! Podemos ver cuántas cosas hay con 'len()'
cantidad_de_cosas = len(cosas_a_mi_alrededor)
print("En esta carpeta hay", cantidad_de_cosas, "archivos o carpetas.")
print("Vamos a verlos uno por uno:\n")

# Usamos el bucle 'for' que aprendimos en niveles anteriores para recorrer la lista
for cosa in cosas_a_mi_alrededor:
    print("- Encontré un objeto llamado:", cosa)


print("\n--- ¡Exploración terminada con éxito! ---")
