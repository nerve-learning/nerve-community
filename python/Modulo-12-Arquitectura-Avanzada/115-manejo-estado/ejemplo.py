# Instalación requerida en terminal: pip install alenia-nerve

from nerve.core import NexusClient, NexusHub
import time

# --- Título de la sección ---
print("--- 1. PREPARANDO EL CEREBRO DEL BOT (EL ESTADO) ---")

# Esta es nuestra "Memoria". Vive AFUERA de las funciones.
# Si estuviera adentro, se borraría con cada mensaje nuevo.
estado_almacen = {
    "manzanas": 50,
    "cajas_vendidas": 0
}

# --- Título de la sección ---
print("--- 2. ENSEÑANDO AL BOT A USAR SU MEMORIA ---")

def bot_de_inventario(payload):
    # payload será algo como {"accion": "vender", "cantidad": 5}
    accion = payload["accion"]
    cantidad = payload["cantidad"]
    
    if accion == "vender":
        # Modificamos el Estado global
        estado_almacen["manzanas"] = estado_almacen["manzanas"] - cantidad
        estado_almacen["cajas_vendidas"] = estado_almacen["cajas_vendidas"] + 1
        
        print(f"🍎 ¡Venta exitosa! Se fueron {cantidad} manzanas.")
        print(f"📊 [ESTADO ACTUAL]: Quedan {estado_almacen['manzanas']} manzanas en stock.")
        print(f"📦 [ESTADO ACTUAL]: Llevamos {estado_almacen['cajas_vendidas']} cajas vendidas.")
    
    elif accion == "reabastecer":
        estado_almacen["manzanas"] = estado_almacen["manzanas"] + cantidad
        print(f"🚚 Llegó el camión. Entraron {cantidad} manzanas nuevas.")
        print(f"📊 [ESTADO ACTUAL]: Quedan {estado_almacen['manzanas']} manzanas en stock.")

# --- Título de la sección ---
print("--- 3. ENCENDIENDO LA RED ---")
# (Solo para que este ejemplo funcione solo, crearemos un mini-hub aquí)
hub = NexusHub()
hub.start()

cliente = NexusClient()
cliente.connect("bot_almacen")
cliente.listen(on_payload=bot_de_inventario)

# --- Título de la sección ---
print("--- 4. SIMULANDO LOS MENSAJES QUE LLEGAN ---")
# Simulamos que otro programa en la red nos envía estos mensajes.
# Nota cómo el bot RECUERDA cuántas manzanas tenía después de cada mensaje.
time.sleep(1)
cliente.send(to="bot_almacen", payload={"accion": "vender", "cantidad": 10})

time.sleep(1)
cliente.send(to="bot_almacen", payload={"accion": "vender", "cantidad": 5})

time.sleep(1)
cliente.send(to="bot_almacen", payload={"accion": "reabastecer", "cantidad": 100})

# Dejamos dormir al programa un segundo para que le dé tiempo a imprimir todo antes de apagarse.
time.sleep(1)
cliente.disconnect()
hub.stop()
