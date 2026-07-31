import time
from nerve import NexusClient

print("--- EL NODO RUIDOSO ---")
print("Para que este ejemplo funcione de verdad, el Hub debe tener configurado")
print("un límite. Por ejemplo: rate_limit_messages_per_sec=2 en nerve.config")

# Conectamos como de costumbre
cliente = NexusClient()
cliente.connect("locutor_agresivo")

print("\n[*] Preparándonos para enviar mensajes rápido...")
print("Vamos a enviar 5 mensajes sin usar time.sleep()...")

try:
    # Bucle rápido que enviará mensajes a la velocidad de la luz
    for i in range(1, 6):
        mensaje = {"mensaje": f"Este es el grito número {i}!"}
        
        # OJO: No hay pausa aquí. La computadora ejecutará esto
        # en milisegundos.
        cliente.broadcast(mensaje)
        print(f"Enviado mensaje {i}")
        
    print("\n[✓] Logré enviar todo (si no había límites).")
    
    # Nos quedamos vivos
    while True:
        time.sleep(1)

except Exception as e:
    # Si el Hub nos patea, nuestra conexión se rompe y Python lanza un error
    print("\n[X] ¡BOOM! Fuimos expulsados de la red por exceso de velocidad.")
    print("El Hub nos detectó como Spam y cerró nuestra conexión.")
    print(f"Error técnico: {e}")
