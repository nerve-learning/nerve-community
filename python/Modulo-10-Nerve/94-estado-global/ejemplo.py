from nerve import NexusClient

print("--- 1. Preparando la Pizarra (Estado Global) ---")
# Esta variable es nuestro estado. Vivirá en la memoria principal.
# Es como el contador de likes de un video de YouTube.
total_likes = 0

print("--- 2. Definiendo al Recepcionista ---")
def procesar_like(caja_de_datos):
    # ¡PERMISO ESPECIAL! Le decimos a Python que queremos editar la pizarra grande.
    # Si quitamos esta línea, el programa explotará en la siguiente línea.
    global total_likes
    
    # Verificamos si el mensaje tiene la instrucción de dar like
    accion = caja_de_datos.get("accion")
    
    if accion == "dar_like":
        # Modificamos el estado global
        total_likes = total_likes + 1
        print(f"❤️ ¡Alguien dio like! Total de likes ahora: {total_likes}")
    else:
        print("Llegó un mensaje, pero no era un like.")


print("--- 3. Conectando y Escuchando ---")
mi_servidor = NexusClient()
mi_servidor.connect("servidor_likes")

# Contratamos al recepcionista pasándole la función SIN paréntesis
mi_servidor.listen(procesar_like)

print("Servidor de likes encendido. Esperando corazones...")
print("(Recuerda que debes tener 'nerve start' corriendo en otra terminal)")

# Bucle infinito para que el servidor nunca se apague
while True:
    # Usamos input para detener el flujo principal.
    # Si escribes 'salir', apagamos el servidor.
    comando = input("")
    if comando == "salir":
        print("Apagando servidor...")
        break # Esto rompe el bucle infinito y el programa termina.
