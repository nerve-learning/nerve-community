# Recuerda instalar: pip install alenia-nerve
from nerve.core import NexusHub, NexusClient
import time

# --- Título de la sección ---
print("--- 1. CONTRATANDO AL CADENERO ---")
# Creamos el Hub pero le ponemos una regla estricta:
# ¡Nadie puede enviar más de 2 mensajes por segundo!
hub = NexusHub(rate_limit_messages_per_sec=2)
hub.start()

policia = NexusClient()
spammer = NexusClient()

policia.connect("policia_central")
spammer.connect("bot_publicidad")

# --- Título de la sección ---
print("--- 2. EL POLICÍA ESCUCHA ---")
mensajes_recibidos = 0

def trabajo_policia(payload):
    # Usamos global para poder modificar la variable que creamos arriba
    global mensajes_recibidos
    mensajes_recibidos = mensajes_recibidos + 1
    print(f"👮 [POLICÍA] Mensaje legítimo recibido: {payload}. (Total: {mensajes_recibidos})")

policia.listen(on_payload=trabajo_policia)

# --- Título de la sección ---
print("--- 3. EL ATAQUE SPAM ---")
print("🤡 [SPAMMER] Voy a enviar 10 mensajes a la velocidad de la luz. ¡Nadie puede detenerme!")

# Usamos un bucle for (Módulo 04) para enviar 10 mensajes rapidísimo,
# sin usar time.sleep.
for i in range(10):
    paquete = {"oferta": f"¡Compra ya! Anuncio #{i}"}
    spammer.send(to="policia_central", payload=paquete)
    
print("🤡 [SPAMMER] ¡Ataque terminado!")

# Le damos tiempo al sistema para procesar
time.sleep(2)

# --- Título de la sección ---
print("--- 4. EL RESULTADO ---")
print(f"🛡️ Gracias al Rate Limit, el policía solo tuvo que leer: {mensajes_recibidos} mensajes.")
print("🛡️ Los demás fueron tirados a la basura por el Hub antes de llegar.")

policia.disconnect()
spammer.disconnect()
hub.stop()
print("🛑 Sistema cerrado.")
