import time
from nerve import NexusClient

# Nuestra memoria compartida en la red
estado_compartido = "Ninguno"

print("--- SISTEMA DE ESTADO SINCRONIZADO ---")
nombre = input("Ingresa tu nombre de nodo (ej. nodo1): ")

cliente = NexusClient()
cliente.connect(nombre)

def al_recibir_mensaje(remitente, mensaje):
    global estado_compartido
    
    # Extraemos la acción que quiere hacer el remitente
    accion = mensaje.get("accion")
    
    if accion == "pedir_sincronizacion":
        # Alguien nuevo entró y pregunta por el estado.
        # Si nosotros tenemos un estado real, se lo compartimos.
        if estado_compartido != "Ninguno":
            print(f"\n[!] {remitente} pidió el estado. Compartiendo: {estado_compartido}")
            respuesta = {
                "accion": "enviar_sincronizacion",
                "datos": estado_compartido
            }
            # Se lo mandamos de vuelta (podríamos usar .send o .broadcast)
            cliente.broadcast(respuesta)
            
    elif accion == "enviar_sincronizacion":
        # ¡Esta es la respuesta a nuestra propia pregunta!
        estado_compartido = mensaje.get("datos")
        print(f"\n[!] ¡Sincronización completada! El estado actual es: {estado_compartido}")
        print("Escribe un nuevo color y presiona Enter: ", end="", flush=True)
        
    elif accion == "actualizar_estado":
        # Alguien cambió el estado de forma normal
        estado_compartido = mensaje.get("datos")
        print(f"\n[*] {remitente} cambió el estado a: {estado_compartido}")
        print("Escribe un nuevo color y presiona Enter: ", end="", flush=True)

# 1. Registramos nuestra oreja electrónica
cliente.listen(al_recibir_mensaje)

# 2. El Handshake (La petición inicial)
# Tan pronto como nos conectamos, gritamos pidiendo el historial
print("[*] Pidiendo sincronización a la red...")
peticion = {
    "accion": "pedir_sincronizacion"
}
cliente.broadcast(peticion)

# Le damos 1 segundo a la red para responder antes de pedirle input al usuario
time.sleep(1)

# 3. El bucle infinito (Nuestro corazón)
print(f"\nEstado actual en tu memoria: {estado_compartido}")
while True:
    nuevo_estado = input("Escribe un nuevo color y presiona Enter: ")
    
    # Actualizamos nuestra propia memoria primero
    estado_compartido = nuevo_estado
    
    # Avisamos a los demás usando la acción 'actualizar_estado'
    mensaje_actualizacion = {
        "accion": "actualizar_estado",
        "datos": estado_compartido
    }
    cliente.broadcast(mensaje_actualizacion)
    print("¡Estado transmitido a la red!")
