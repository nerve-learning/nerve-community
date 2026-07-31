# Importante: Asegúrate de tener Nerve instalado antes de empezar.
# En tu terminal ejecuta: pip install alenia-nerve

from nerve.core import NexusHub, NexusClient
import time

# --- Título de la sección ---
print("--- 1. CREANDO EL SALVAVIDAS (EL HUB) ---")

# Creamos el Hub pero no usamos el valor por defecto de 5 segundos.
# Le decimos que revise el pulso cada 2.5 segundos para detectar caídas más rápido.
# El parámetro debe ser un número (int o float), sin comillas.
salvavidas_hub = NexusHub(heartbeat_interval=2.5)

# Encendemos el servidor en segundo plano
salvavidas_hub.start()
print("🏥 El Hub Salvavidas está encendido. Revisará el pulso cada 2.5 segundos.")

# --- Título de la sección ---
print("--- 2. EL NADADOR ENTRA AL AGUA (EL CLIENTE) ---")

# Creamos un cliente normal, el cliente automáticamente sabe cómo
# responder a los latidos sin que nosotros programemos nada extra.
nadador = NexusClient()
nadador.connect("nadador_01")
print("🏊 El 'nadador_01' se ha conectado al Hub.")

# --- Título de la sección ---
print("--- 3. OBSERVANDO LOS LATIDOS ---")
print("⏳ Esperando 6 segundos... El Hub y el Cliente se están saludando en secreto por debajo.")

# Hacemos que nuestro programa principal se duerma 6 segundos
# Durante este tiempo, el Hub revisará el pulso del nadador unas 2 veces.
# (2.5 seg y luego a los 5.0 seg).
time.sleep(6)
print("✅ Si el programa no ha explotado, los latidos funcionan perfecto.")

# --- Título de la sección ---
print("--- 4. CERRANDO EL PARQUE ACUÁTICO ---")
# Siempre es importante ser ordenados y apagar lo que encendemos.
nadador.disconnect()
salvavidas_hub.stop()
print("🛑 Todos desconectados. Programa terminado limpiamente.")
