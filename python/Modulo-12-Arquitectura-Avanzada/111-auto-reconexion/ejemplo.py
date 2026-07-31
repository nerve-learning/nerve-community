# Recuerda instalar nerve primero en tu terminal:
# pip install alenia-nerve

# Importamos la herramienta NexusClient de Nerve
from nerve.core import NexusClient

# --- Título de la sección ---
print("--- 1. PREPARANDO NUESTRO AVIÓN (FUNCIONES) ---")

# Esta es la función que procesa los mensajes normales, como ya sabes.
# Nerve le pasará el 'payload' (el contenido del mensaje) cuando llegue algo.
def procesar_mensaje(payload):
    print(f"📩 ¡Mensaje recibido desde el Hub!: {payload}")

# ¡Esta es la novedad! Una función que no recibe parámetros.
# Solo existe para celebrar que sobrevivimos a una desconexión.
def avisar_reconexion():
    print("🔌 ¡Bzzzt! ¡La energía ha vuelto!")
    print("✅ ¡El cliente se ha reconectado automáticamente al Hub!")

# --- Título de la sección ---
print("--- 2. ENCENDIENDO EL CLIENTE ---")

# Creamos nuestro cliente y le damos un nombre. Este es nuestro avión.
cliente = NexusClient()

# Nos conectamos al Hub. Si el Hub no está encendido en este momento,
# se conectará igual, pero Nerve se quedará intentando por debajo.
print("⏳ Intentando conectar al Hub de Nerve...")
cliente.connect("nodo_superviviente")
print("✅ Conectado y listo.")

# --- Título de la sección ---
print("--- 3. MODO ESCUCHA CON AUTO-RECONEXIÓN ---")
print("🎧 Escuchando mensajes. Si el Hub se apaga, no entraré en pánico.")
print("   (Prueba apagar el Hub y volver a encenderlo, verás la magia)")

# Aquí le entregamos nuestras dos herramientas a Nerve.
# 1. on_payload: Le damos la herramienta para procesar datos.
# 2. on_reconnect: Le damos la herramienta para avisar cuando vuelva la luz.
# ¡Nota que no hay paréntesis al final de los nombres de las funciones!
cliente.listen(
    on_payload=procesar_mensaje,
    on_reconnect=avisar_reconexion
)
