import time
from nerve import NexusClient

print("--- Iniciando Generador de Tráfico Pesado ---")
print("Asegúrate de estar mirando tu terminal de 'nerve monitor'")

# Creamos nuestro cliente
robot_trabajador = NexusClient()

# Nos conectamos a la red local (El Hub ya debe estar corriendo)
robot_trabajador.connect("generador_de_carga")

print("\n--- Inundando la red de mensajes ---")
print("Empezaremos a enviar muchísimos mensajes...")
print("Observa cómo suben los números en el monitor.")

# Vamos a enviar 5000 mensajes extremadamente rápido
for i in range(1, 5001):
    # Un paquete de datos simple
    paquete = {"id_mensaje": i, "texto": "Prueba de estrés del sistema"}
    
    # Enviamos el paquete al destino "servidor_destino"
    # Nota: No importa si "servidor_destino" no existe, el Hub descartará el mensaje,
    # pero el monitor AÚN registrará que enviamos tráfico.
    robot_trabajador.send("servidor_destino", paquete)
    
    # Imprimimos en pantalla solo cada 1000 mensajes para no saturar nuestra consola
    if i % 1000 == 0:
        print(f"Enviados {i} mensajes...")
        # Pequeña pausa para que el monitor alcance a graficar el pico de tráfico
        time.sleep(1)

print("\n--- Finalizando ---")
print("Se han enviado todos los mensajes.")
print("Verás que nuestro cliente seguirá conectado y vivo en el monitor por 10 segundos más.")

# Mantenemos vivo el programa 10 segundos para que no desaparezca del monitor inmediatamente
time.sleep(10)
print("Apagando...")
