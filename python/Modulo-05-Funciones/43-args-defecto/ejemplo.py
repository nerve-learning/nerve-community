print("--- 1. Función con Parámetro por Defecto ---")

# 'mensaje' es obligatorio.
# 'simbolo' es opcional. Si no nos dan uno, usaremos un asterisco '*'.
def enmarcar_texto(mensaje, simbolo="*"):
    borde = simbolo * 20
    print(borde)
    print(mensaje)
    print(borde)
    print("") # Línea en blanco

# Llamada 1: Solo damos el mensaje. 
# Python usa el '*' por defecto para el símbolo.
print("Llamada 1 (Solo mensaje):")
enmarcar_texto("¡Hola Mundo!")

# Llamada 2: Damos ambos. 
# El '=' sobreescribe al '*' porque nosotros se lo ordenamos.
print("Llamada 2 (Mensaje y símbolo nuevo):")
enmarcar_texto("¡PELIGRO!", "=")

# Llamada 3: Otro símbolo diferente
print("Llamada 3 (Mensaje y otro símbolo):")
enmarcar_texto("Victoria", "~")


print("--- 2. Creación de Usuarios (Múltiples Defectos) ---")

# 'nombre' es obligatorio.
# 'pais' y 'suscripcion' son opcionales.
def registrar_usuario(nombre, pais="Desconocido", suscripcion="Gratis"):
    print("Nuevo usuario:", nombre)
    print("Origen:", pais)
    print("Plan:", suscripcion)
    print("--------------------")

# Pasamos solo el obligatorio. Los otros dos usan el Plan B.
registrar_usuario("Alejandro")

# Pasamos dos datos. Python los asigna de izquierda a derecha:
# "María" va a 'nombre'. "México" va a 'pais'. 'suscripcion' usa el Plan B.
registrar_usuario("María", "México")

# Pasamos los tres datos. Ninguno usa el Plan B.
registrar_usuario("Carlos", "Argentina", "Premium")

# (En el próximo nivel veremos cómo saltarnos el orden para cambiar solo 
# la suscripción sin cambiar el país, pero por ahora, siempre va de izquierda a derecha).
