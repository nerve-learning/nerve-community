from nerve import NexusClient
import time

client = NexusClient()

client.connect("test2")


# Escuchar mensajes entrantes
def on_message(data):
    print(f"Recibido: {data}")


print("Escuchando eventos en tiempo real... (Presiona Ctrl+C para salir)")
try:
    while True:
        client.listen(on_message)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nDesconectando clientes...")
    client.disconnect()
