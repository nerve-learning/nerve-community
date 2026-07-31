# Recuerda: pip install alenia-nerve
from nerve.core import NexusHub, NexusClient
import time

# --- Título de la sección ---
print("--- 1. ENCENDIENDO LA FÁBRICA ---")
hub = NexusHub()
hub.start()

# Vamos a crear 3 bots diferentes. En la vida real, cada uno podría estar
# corriendo en una computadora distinta en partes diferentes del mundo.
# Aquí los correremos en el mismo archivo para aprender.
bomba = NexusClient()
filtro = NexusClient()
embotelladora = NexusClient()

bomba.connect("bomba_agua")
filtro.connect("filtro_purificador")
embotelladora.connect("embotelladora_final")

# --- Título de la sección ---
print("--- 2. CREANDO LOS ESLABONES DEL PIPELINE ---")

# ESLABÓN 2: EL FILTRO
# Recibe agua sucia, la limpia, y la manda a la embotelladora.
def trabajo_del_filtro(payload):
    print(f"🧽 [FILTRO] Recibí: {payload['estado']}. Limpiando...")
    time.sleep(1) # Simulamos que toma tiempo limpiar
    
    # Transformamos el dato
    payload["estado"] = "Agua Limpia"
    
    # ¡CRÍTICO! Pasamos el paquete al siguiente eslabón
    filtro.send(to="embotelladora_final", payload=payload)

# ESLABÓN 3: LA EMBOTELLADORA
# Recibe agua limpia, la embotella y termina el proceso.
def trabajo_de_embotelladora(payload):
    print(f"🍾 [EMBOTELLADORA] Recibí: {payload['estado']}. Envasando...")
    time.sleep(1)
    
    payload["estado"] = "Botella de Agua Lista para Vender"
    print(f"✅ [ÉXITO] Producto final terminado: {payload}")

# --- Título de la sección ---
print("--- 3. CONECTANDO LAS MÁQUINAS ---")
# Le decimos a las máquinas que escuchen.
filtro.listen(on_payload=trabajo_del_filtro)
embotelladora.listen(on_payload=trabajo_de_embotelladora)

# --- Título de la sección ---
print("--- 4. ARRANCANDO LA CADENA DE MONTAJE ---")
# ESLABÓN 1: LA BOMBA
# La bomba no escucha a nadie, ella INICIA el pipeline. Extrae el agua y la empuja.
agua_extraida = {"origen": "Rio", "estado": "Agua Sucia y Lodosa"}

print(f"🌊 [BOMBA] Extrayendo agua del río y enviándola al filtro...")
bomba.send(to="filtro_purificador", payload=agua_extraida)

# Dejamos que la magia ocurra por unos segundos antes de cerrar
time.sleep(4)

bomba.disconnect()
filtro.disconnect()
embotelladora.disconnect()
hub.stop()
print("🛑 Fábrica cerrada correctamente.")
