# ==========================================
# NIVEL 110: Instaladores Mágicos
# ==========================================
# En este ejemplo, crearemos un pequeño "Instalador" 
# que configurará la computadora del usuario automáticamente.

# 1. Traemos a nuestro traductor del sistema
import os

print("--- Iniciando el Instalador Mágico ---")
print("Hola, usuario. Preparando tu computadora para abrir cajas fuertes...")

# 2. Le pedimos a Python que asocie los archivos .nrv
# Esto hará que los archivos .nrv se abran con Nerve al hacer doble clic.
# La función os.system() ejecuta el comando como si lo escribiéramos en la terminal.
os.system("nerve associate")

print("¡Asociación completada!")

# 3. Vamos a crear un archivo de prueba para que el usuario pueda probar el doble clic.
print("\n--- Creando un archivo de prueba ---")

# Usaremos un comando rápido de terminal (echo) para crear un archivo falso de prueba
# Solo para que el usuario pueda ver el ícono bonito en su carpeta.
# Nota: Esto crea un archivo de texto normal, pero con extensión .nrv
os.system("echo 'Contenido secreto' > mi_caja_fuerte_de_prueba.nrv")

print("¡He creado 'mi_caja_fuerte_de_prueba.nrv' en esta carpeta!")
print("Ve a tu explorador de archivos y haz doble clic sobre él.")
print("Verás que Nerve intenta abrirlo automáticamente.")
