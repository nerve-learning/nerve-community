from nerve import NexusClient

# Paso 1: Configurar la antena
mi_chat = NexusClient()

# ¡OJO! Recuerda tener corriendo "nerve start" en OTRA terminal.
mi_chat.connect("jugador_1")
print("¡Conectados a la red local como 'jugador_1'!")

print("--- 1. Configurando el Altavoz (Recepcionista) ---")

# Esta función es nuestra oreja. Siempre que alguien nos envíe un paquete,
# Nerve se lo pasará a esta función automáticamente en segundo plano.
def altavoz(caja_de_datos):
    # Intentamos sacar el texto del diccionario. Si no existe la llave "texto", usamos un valor por defecto.
    mensaje = caja_de_datos.get("texto", "Mensaje ilegible...")
    origen = caja_de_datos.get("de_quien", "Desconocido")
    
    # Imprimimos el mensaje. El \n al principio es para dar un salto de línea 
    # y que no se junte feo con lo que nosotros estamos escribiendo.
    print(f"\n💬 [{origen}] dice: {mensaje}")

# Contratamos al recepcionista (¡AFUERA del bucle!)
mi_chat.listen(altavoz)
print("Altavoz encendido. Escuchando mensajes...")


print("--- 2. Configurando el Micrófono (Bucle P2P) ---")
print("Escribe tus mensajes abajo. Presiona Ctrl+C para salir.\n")

# Bucle infinito: este código se repetirá por siempre.
# Mientras estamos pausados en el "input", nuestro altavoz en segundo plano sigue trabajando.
while True:
    # 1. Leemos lo que el usuario escribe en la consola
    mi_texto = input("Tú: ")
    
    # 2. Armamos la caja (diccionario) con nuestro texto y nuestro nombre
    paquete = {
        "texto": mi_texto,
        "de_quien": "jugador_1"
    }
    
    # 3. Enviamos el paquete al "jugador_2" (incluso si no existe todavía, Nerve lo maneja)
    mi_chat.send("jugador_2", paquete)
