import time
from nerve import NexusClient

print("--- Iniciando Programa Espía ---")

# Creamos al cliente que enviará mensajes
emisor = NexusClient()

try:
    print("Intentando conectar con el Hub...")
    # Nos conectamos a la red local con un nombre único
    emisor.connect("agente_007")
    print("¡Conexión exitosa!")
    
    print("\n--- Enviando Datos Confidenciales ---")
    
    # Enviamos 5 mensajes secretos al destino "cuartel_general"
    for i in range(1, 6):
        mensaje_secreto = {"operacion": "Mision Imposible", "paso": i}
        emisor.send("cuartel_general", mensaje_secreto)
        print(f"Paquete {i} enviado al cuartel.")
        
        # Pausa de 1 segundo para que lo puedas ver lentamente en el Hub
        time.sleep(1)

    print("\n--- Desconexión ---")
    print("El trabajo está hecho. Mi programa se cerrará.")

except ConnectionRefusedError:
    print("❌ ALERTA ROJA: No pude encontrar la Oficina de Correos.")
    print("¿Olvidaste abrir otra terminal y escribir 'nerve start --verbose'?")
