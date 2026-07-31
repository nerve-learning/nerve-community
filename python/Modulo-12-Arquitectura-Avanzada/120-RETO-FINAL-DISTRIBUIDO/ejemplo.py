import time
import sys
from nerve.core import NexusClient

print("--- INICIANDO NODO DEL SISTEMA ---")
print("Para que esto funcione, primero debiste ejecutar 'nerve start' en otra terminal.")
print("¿Qué rol debe tomar este script hoy?")
print("1. El Sensor (Grita datos)")
print("2. La Pantalla (Escucha datos)")
opcion = input("Escribe 1 o 2: ")

print("--- CONECTANDO AL CEREBRO ---")
# Creamos el cliente de red. Como no le pasamos parámetros mágicos,
# asume que el hub central está corriendo en tu misma compu (localhost).
cliente = NexusClient()
cliente.connect("nodo_camaleon")

if opcion == "1":
    print("--- MODO SENSOR ACTIVADO ---")
    print("Enviando un dato por segundo. Abre otra terminal con la opción 2 para verlos.")
    contador = 1
    
    # Un bucle infinito para mandar datos sin parar
    while True:
        try:
            # Mandamos un diccionario con la información del sensor
            paquete = {
                "tipo": "temperatura",
                "valor": contador,
                "mensaje": "¡Hace calor!"
            }
            
            # broadcast() grita el mensaje a todos los conectados
            cliente.broadcast(paquete)
            print(f"📡 Enviado: {contador} grados...")
            
            contador = contador + 1
            # Pausamos 1 segundo para no explotar la computadora
            time.sleep(1)
            
        except KeyboardInterrupt:
            # Si el humano presiona Ctrl+C, salimos de forma elegante
            print("\nApagando sensor...")
            break

elif opcion == "2":
    print("--- MODO PANTALLA ACTIVADO ---")
    print("Esperando señales del sensor en silencio...")
    
    # Esta es nuestra "oreja". Cada que llegue un mensaje, se ejecuta esta función.
    def procesar_senal(mensaje):
        # mensaje es un diccionario que envió el sensor
        grados = mensaje["valor"]
        alerta = mensaje["mensaje"]
        print(f"📺 PANTALLA RECIBIÓ: La temperatura es {grados}° -> {alerta}")

    # Le decimos al cliente que empiece a escuchar y use nuestra "oreja"
    cliente.listen(procesar_senal)
    
    # Mantener el programa vivo. Si no ponemos esto, el script se cierra de inmediato.
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nApagando pantalla...")

else:
    print("Opción inválida. Intenta de nuevo.")

# Siempre es de buena educación desconectarse al terminar
cliente.disconnect()
print("--- NODO DESCONECTADO ---")
