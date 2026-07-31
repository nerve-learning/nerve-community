from nerve import NexusClient

print("--- 1. Definiendo al Recepcionista ---")
# Creamos la función que se encargará de abrir los paquetes cuando lleguen.
# Nerve siempre nos enviará el contenido en el primer parámetro, lo llamaremos 'caja_de_datos'.
def abrir_paquete(caja_de_datos):
    print("\n[🔔 RING RING] ¡El tubo neumático acaba de escupir un paquete!")
    
    # Extraemos algo del diccionario (asumiendo que quien envía usa estas llaves)
    # Usamos .get() por si acaso no viene esa llave, así no explota el programa.
    origen = caja_de_datos.get("de", "Alguien anónimo")
    mensaje = caja_de_datos.get("mensaje", "Caja vacía...")
    
    print(f"[{origen} dice]: {mensaje}")
    print("---------------------------------------------------")


print("--- 2. Preparando la Antena ---")
mi_nodo = NexusClient()

# Recuerda: El Hub (nerve start) debe estar encendido en otra terminal
mi_nodo.connect("nodo_receptor")
print("¡Conectados! Somos conocidos como 'nodo_receptor'.")

print("--- 3. Contratando al Recepcionista ---")
# Le decimos a Nerve: "Oye, cuando llegue cualquier cosa, dásela a 'abrir_paquete'".
# ¡Fíjate bien! NO tiene paréntesis al final.
mi_nodo.listen(abrir_paquete)
print("Recepcionista contratado. Las orejas están abiertas.")


print("--- 4. Manteniendo el programa vivo ---")
# Si el código termina aquí, Python cerrará la ventana y nuestro recepcionista morirá.
# Usamos un input para "congelar" el programa principal. 
# Mientras está congelado aquí, el recepcionista en segundo plano sigue trabajando.
input("El nodo está escuchando 24/7... (Presiona ENTER en esta ventana para apagarlo)\n")

print("Apagando el nodo. ¡Adiós!")
