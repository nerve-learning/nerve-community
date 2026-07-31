# Recuerda instalar: pip install alenia-nerve
from nerve.core import NexusHub, NexusClient
import time

# --- Título de la sección ---
print("--- 1. ENCENDIENDO EL SISTEMA BANCARIO ---")
hub = NexusHub()
hub.start()

cajero = NexusClient()
banco = NexusClient()

cajero.connect("cajero_01")
banco.connect("servidor_central")

# Esta es la "memoria" del cajero. Aquí anota lo que está esperando.
# Usamos un diccionario donde la llave es el ID del mensaje.
transacciones_pendientes = {}

# --- Título de la sección ---
print("--- 2. CREANDO LAS DEFENSAS DEL BANCO ---")

def trabajo_del_banco(payload):
    print(f"🏦 [BANCO] Recibí petición: {payload}")
    
    # Usamos try/except como escudo. Si el cajero envía basura, el banco NO MUERE.
    try:
        id_peticion = payload["id_transaccion"]
        monto = payload["monto"]
        
        # Simulamos que procesamos el retiro
        print(f"🏦 [BANCO] Procesando retiro de ${monto}...")
        time.sleep(1) # Toma tiempo conectar con la bóveda
        
        # ¡EL ACK! Confirmamos que todo salió bien
        respuesta_ack = {
            "tipo": "ACK", 
            "id_transaccion": id_peticion, 
            "status": "APROBADO"
        }
        banco.send(to="cajero_01", payload=respuesta_ack)
        print("🏦 [BANCO] Envié confirmación (ACK).")
        
    except Exception as e:
        print(f"🚨 [BANCO] Recibí un mensaje malformado. Error: {e}")
        # Opcional: Podríamos enviar un NACK (Negative Acknowledge) aquí.

# --- Título de la sección ---
print("--- 3. EL CAJERO ESCUCHANDO CONFIRMACIONES ---")

def cajero_escucha(payload):
    # El cajero solo debe reaccionar si es un ACK
    if payload.get("tipo") == "ACK":
        id_confirmado = payload["id_transaccion"]
        estado = payload["status"]
        
        # Revisamos si estábamos esperando este ID
        if id_confirmado in transacciones_pendientes:
            print(f"🏧 [CAJERO] ¡Confirmación recibida! Transacción {id_confirmado} dice: {estado}")
            # Lo borramos de los pendientes porque ya se completó
            del transacciones_pendientes[id_confirmado]
            print(f"🏧 [CAJERO] Entregando billetes al cliente. Pendientes restantes: {len(transacciones_pendientes)}")

banco.listen(on_payload=trabajo_del_banco)
cajero.listen(on_payload=cajero_escucha)

# --- Título de la sección ---
print("--- 4. SIMULANDO LA OPERACIÓN ---")

# 1. El cajero genera una petición con ID único
id_unico = 999
peticion_retiro = {
    "id_transaccion": id_unico,
    "monto": 500
}

# 2. La anota en su memoria ANTES de enviarla
transacciones_pendientes[id_unico] = "Esperando confirmación del banco..."
print(f"🏧 [CAJERO] Generé transacción {id_unico}. Pendientes actuales: {len(transacciones_pendientes)}")

# 3. La envía al banco
cajero.send(to="servidor_central", payload=peticion_retiro)

# Damos tiempo para que el mensaje viaje, el banco procese y el ACK regrese
time.sleep(3)

print("--- 5. PRUEBA DE FUEGO (EL MENSAJE ENVENENADO) ---")
# Enviamos basura para ver si el banco sobrevive
cajero.send(to="servidor_central", payload={"soy": "un hacker, rompe tu sistema!"})

time.sleep(2)

cajero.disconnect()
banco.disconnect()
hub.stop()
print("🛑 Sistema cerrado.")
