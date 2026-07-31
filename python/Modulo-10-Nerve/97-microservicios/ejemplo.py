import time
from nerve import NexusClient

print("--- EL RESTAURANTE DIGITAL ---")
print("Tenemos dos roles en este restaurante:")
print("1. mesero (Toma las órdenes y las envía)")
print("2. chef (Recibe las órdenes y las cocina)")
rol = input("¿Qué rol quieres jugar? (escribe 'mesero' o 'chef'): ")

# Conectamos nuestro nodo con el nombre del rol que elegimos
cliente = NexusClient()
cliente.connect(rol)

if rol == "chef":
    print("--- MODO CHEF ACTIVADO ---")
    print("[*] Esperando órdenes en la cocina...")
    
    # El chef necesita orejas para escuchar las órdenes
    def al_recibir_orden(remitente, mensaje):
        accion = mensaje.get("accion")
        if accion == "cocinar":
            plato = mensaje.get("plato")
            print(f"\n[!] Orden recibida de {remitente}: {plato}")
            print(f"[*] Cocinando {plato}...")
            
            # Simulamos que cocinar toma tiempo
            time.sleep(3)
            
            print(f"[✓] {plato} terminado. Avisando al mesero.")
            # Le enviamos un mensaje privado de vuelta al mesero
            respuesta = {
                "accion": "comida_lista",
                "plato": plato
            }
            cliente.send("mesero", respuesta)

    # Registramos la oreja
    cliente.listen(al_recibir_orden)
    
    # El chef solo se queda esperando infinitamente
    while True:
        time.sleep(1)

elif rol == "mesero":
    print("--- MODO MESERO ACTIVADO ---")
    
    # El mesero también necesita escuchar cuando la comida esté lista
    def al_recibir_campana(remitente, mensaje):
        accion = mensaje.get("accion")
        if accion == "comida_lista":
            plato = mensaje.get("plato")
            print(f"\n[🔔] DING! El chef dice que la orden de '{plato}' está lista.")
            print("¿Qué plato quiere el cliente?: ", end="", flush=True)
            
    cliente.listen(al_recibir_campana)
    
    # El mesero toma órdenes infinitamente
    while True:
        orden = input("¿Qué plato quiere el cliente?: ")
        
        # Preparamos el paquete de información
        paquete = {
            "accion": "cocinar",
            "plato": orden
        }
        
        # En vez de gritarle a todo el restaurante (.broadcast), 
        # le hablamos directo al "chef"
        print("[*] Enviando orden directamente al chef...")
        cliente.send("chef", paquete)

else:
    print("Rol no reconocido. Debes ser 'mesero' o 'chef'.")
