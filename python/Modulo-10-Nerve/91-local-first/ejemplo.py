import time # Traemos 'time' para poder hacer que el programa espere un poquito al final

# Paso 0: Importamos la antena de Nerve
# (Recuerda: si esto falla, debes hacer 'pip install alenia-nerve' en la terminal)
from nerve import NexusClient

print("--- 1. Preparando la Antena ---")
# Creamos nuestro transmisor. Es como comprar el radio en la tienda.
mi_radio = NexusClient()

print("--- 2. Conectando a la red local ---")
# ¡ATENCIÓN! Para que esta línea funcione, debes tener OTRA terminal abierta
# donde hayas escrito: nerve start
# Si no, el radio no tendrá a dónde conectarse.
mi_radio.connect("aprendiz_python")
print("¡Conectados con éxito! Nuestro programa ahora tiene voz propia en la red Nerve.")

print("--- 3. Enviando un mensaje directo ---")
# Armamos una caja (diccionario) con los datos que queremos enviar.
# Las redes de Nerve aman los diccionarios, viajan muy cómodos por el tubo.
caja_de_datos = {
    "mensaje": "¡Hola, mundo local!",
    "nivel": 91,
    "estado": "muy emocionado"
}

# Usamos .send() para mandar la caja a un destino específico.
# El primer parámetro ("pantalla_principal") es el nombre del gafete del que recibe.
# El segundo parámetro es nuestra caja.
# Nota: Si "pantalla_principal" no está conectado aún, Nerve lo guardará o lo descartará según configuremos, ¡pero nuestro envío no falla!
mi_radio.send("pantalla_principal", caja_de_datos)
print("Paquete directo enviado por el tubo neumático.")

print("--- 4. Avisando a todos (Megáfono) ---")
# .broadcast() no necesita un nombre de destino. Es un grito para toda la red.
# Cualquier otro programa conectado a Nerve escuchará esto.
mi_radio.broadcast({"aviso_general": "¡He dado mi primer paso en Nerve y Local-First!"})
print("Grito con megáfono enviado a toda la red.")

print("--- Fin del Ejemplo ---")
# Le damos 1 segundo al programa para que espere y los mensajes terminen 
# de viajar por los cables locales antes de que Python se cierre de golpe.
time.sleep(1)
