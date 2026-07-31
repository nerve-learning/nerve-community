# ==========================================
# NIVEL 06: ESCUCHANDO AL HUMANO
# ==========================================

print("--- Inicializando protocolo de entrevista ---")

# La computadora mostrará el texto, se pausará y esperará.
# Lo que escribas se guardará en la caja 'usuario'.
usuario = input("Por favor, ingresa tu nombre de piloto: ")

# Pedimos otro dato más. 
# Nota el espacio extra al final de la pregunta ("...favorito: ").
# Esto es para que al escribir, el texto no quede pegado a los dos puntos.
color_traje = input("¿Cuál es tu color de traje favorito? ")

print("--- Procesando información ---")

# Ahora usamos la orden print() para combinar nuestros textos
# con las respuestas que el humano guardó en las cajas.
print("Bienvenido a bordo,")
print(usuario)

print("Hemos preparado tu traje color:")
print(color_traje)

print("¡Preparación completada!")
