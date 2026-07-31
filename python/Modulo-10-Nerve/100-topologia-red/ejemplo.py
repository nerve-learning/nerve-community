import time
import threading
from nerve import NexusClient

def crear_nodo(nombre_nodo):
    """
    Esta función crea un cliente y lo conecta al Hub.
    Luego lo deja vivo durante 60 segundos.
    """
    cliente = NexusClient()
    
    try:
        # Intentamos conectar al Hub
        cliente.connect(nombre_nodo)
        print(f"[{nombre_nodo}] Conectado a la topología estrella.")
        
        # Mantenemos vivo el nodo para que lo podamos ver en el dashboard
        time.sleep(60)
        
    except ConnectionRefusedError:
        print(f"[{nombre_nodo}] ¡Error! No pude encontrar al Hub. ¿Ejecutaste 'nerve start'?")

# Vamos a crear 3 hilos diferentes simulando 3 programas independientes
hilo1 = threading.Thread(target=crear_nodo, args=("visor_grafico",))
hilo2 = threading.Thread(target=crear_nodo, args=("motor_ia",))
hilo3 = threading.Thread(target=crear_nodo, args=("base_de_datos_local",))

print("Iniciando la población de la red...")

# Arrancamos los hilos
hilo1.start()
hilo2.start()
hilo3.start()

# Esperamos a que los hilos terminen su trabajo de 60 segundos
hilo1.join()
hilo2.join()
hilo3.join()

print("Fin de la simulación.")
