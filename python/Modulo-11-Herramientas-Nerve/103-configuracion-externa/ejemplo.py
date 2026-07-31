import time
import os
from nerve import NexusClient

print("--- Paso 1: Preparando el Plano de la Casa ---")

# Vamos a crear el archivo nerve.config directamente desde Python
# para asegurarnos de que exista antes de intentar conectar.
# En la vida real, crearías este archivo a mano en tu editor de texto.

configuracion = """port=60606
socket_path=/tmp/red_rebelde.sock
"""

# Abrimos un archivo llamado nerve.config en modo escritura ("w")
with open("nerve.config", "w") as archivo:
    archivo.write(configuracion)
    print("Archivo 'nerve.config' creado exitosamente.")

print("\n--- Paso 2: Conectando a la Nueva Dirección ---")
print("⚠️ ADVERTENCIA: Si no has iniciado 'nerve start' en esta misma carpeta, esto fallará.")

try:
    # Fíjate cómo NO le pasamos ninguna dirección aquí.
    # El NexusClient es lo suficientemente inteligente para buscar el archivo nerve.config por sí solo.
    cliente_rebelde = NexusClient()
    cliente_rebelde.connect("nave_espacial")
    
    print("¡Éxito! Nos conectamos a la red rebelde.")
    
    # Enviamos un mensaje rápido
    cliente_rebelde.send("base", {"estado": "En órbita"})
    time.sleep(2)

except ConnectionRefusedError:
    print("❌ Error: No se encontró el Hub.")
    print("Recuerda que debes ejecutar 'nerve start' estando en ESTA MISMA CARPETA,")
    print("para que el Hub lea el nerve.config que acabamos de crear.")
