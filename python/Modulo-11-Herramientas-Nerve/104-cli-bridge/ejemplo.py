import time
from nerve import NexusClient

# Este es un trabajador normal dentro de la oficina de Nerve.
# No sabe, ni le importa, si los mensajes vienen de otro script de Python
# o desde una página web a través del "nerve bridge".
# Para él, todos los mensajes se ven iguales.

# 1. Creamos al trabajador
trabajador = NexusClient()

# 2. Se conecta a la oficina (el Hub debe estar corriendo)
print("Trabajador intentando entrar a la oficina...")
trabajador.connect("procesador_web")

# 3. Definimos qué hacer cuando llegue un mensaje (sin importar quién lo envíe)
def al_recibir_mensaje(datos):
    print(f"\n¡El trabajador recibió un mensaje de la red!")
    print(f"Contenido: {datos}")
    print("¡Trabajo completado!")

# 4. Le decimos al trabajador que preste atención
trabajador.listen(al_recibir_mensaje)

# Mantenemos el programa vivo para que el trabajador pueda esperar mensajes
print("Trabajador en su escritorio, esperando mensajes...")
while True:
    time.sleep(1)
