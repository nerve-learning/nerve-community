# Importamos nuestra caja de herramientas del sistema operativo
import os

print("--- 1. Activando el Mapa Visual ---")
print("En un momento, le pediremos a Nerve que inicie su interfaz web.")
print("Tu código de Python se 'pausará' en la siguiente orden porque el dashboard es infinito.")

print("\n👇 INSTRUCCIONES 👇")
print("1. Cuando veas que esto se detiene, abre Google Chrome o tu navegador.")
print("2. Escribe en la barra de direcciones: http://localhost:8080")
print("3. Juega un poco con la interfaz que aparecerá.")
print("4. Vuelve a esta ventana de código y presiona la combinación 'Ctrl + C' para salir.")
print("------------------\n")

# Ejecutamos el servidor web integrado de Nerve
comando = "nerve dashboard"
print(f"Ejecutando: {comando} ...")

os.system(comando)

# Esta línea SOLO se imprimirá si el estudiante presionó Ctrl + C correctamente.
# (En algunos sistemas, Ctrl+C corta todo el script de Python, pero en otros 
# solo corta el os.system y continúa aquí. ¡De cualquier forma es un éxito!).
print("\n--- 2. Freno de emergencia exitoso ---")
print("¡Felicidades! Acabas de encender y apagar un proceso continuo como todo un experto.")
