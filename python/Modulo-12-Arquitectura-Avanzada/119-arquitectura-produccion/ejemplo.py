# Recuerda: pip install alenia-nerve
from nerve.core import NexusClient
import time

# --- INSTRUCCIONES VITALES ANTES DE EJECUTAR ---
print("¡ALTO AHÍ! 🛑")
print("Para que este código funcione, NO debe haber un NexusHub() creado aquí.")
print("1. Abre OTRA terminal en tu computadora.")
print("2. Escribe el comando: nerve start")
print("3. Una vez que veas el banner morado del Hub, regresa a esta terminal y corre este archivo.")
print("---------------------------------------------------------")

# Pausa de 5 segundos por si olvidaste abrir el Hub, te dé tiempo de leer y cancelar (Ctrl+C).
time.sleep(5) 

# --- Título de la sección ---
print("--- 1. CONECTANDO AL HUB EXTERNO ---")
# Estos clientes buscarán conectarse al Hub que abriste en tu otra terminal.
# Magia: Si hubieras creado un archivo nerve.config, lo leerían automáticamente.
sensor_clima = NexusClient()
pantalla_datos = NexusClient()

# Si el Hub no está encendido en la otra terminal, esto lanzará el temido
# error "Connection Refused".
print("🔌 Conectando trabajadores a la red...")
sensor_clima.connect("sensor_01")
pantalla_datos.connect("pantalla_01")

# --- Título de la sección ---
print("--- 2. EL TRABAJO DESACOPLADO ---")
def mostrar_datos(payload):
    clima = payload["clima"]
    print(f"📺 [PANTALLA] Actualización recibida del exterior: El clima es {clima}")

pantalla_datos.listen(on_payload=mostrar_datos)

print("🌡️ [SENSOR] Leyendo clima y enviándolo a la red...")
sensor_clima.send(to="pantalla_01", payload={"clima": "Soleado con 25°C"})

# Damos tiempo a la comunicación
time.sleep(2)

# --- Título de la sección ---
print("--- 3. FIN DE LA JORNADA ---")
sensor_clima.disconnect()
pantalla_datos.disconnect()
print("🛑 Trabajadores desconectados.")
print("¡Fíjate en tu otra terminal! El comando 'nerve start' SIGUE VIVO esperando nuevos clientes.")
