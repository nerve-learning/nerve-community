print("--- 1. Creando nuestro Diario Protegido ---")

class DiarioIntimo:
    def __init__(self, clave):
        # Esta es una variable PÚBLICA. No tiene guiones bajos al inicio.
        self.dueño = "Alejandro"
        
        # Estas son variables PRIVADAS. Llevan __ al inicio.
        # Están protegidas; solo el diario sabe que existen.
        self.__secreto = "Le tengo miedo a las mariposas."
        self.__clave = clave

    # Este es un método (botón) PÚBLICO. 
    # Como pertenece a la clase, SÍ tiene permiso para leer los secretos.
    def leer_secreto(self, intento_clave):
        # Aquí verificamos si el usuario tiene permiso antes de soltar la sopa
        if intento_clave == self.__clave:
            print(f"🔓 Acceso concedido. El secreto es: {self.__secreto}")
        else:
            print("🚨 ¡CONTRASEÑA INCORRECTA! ALARMA ACTIVADA.")


print("--- 2. Creando el Objeto ---")

mi_diario = DiarioIntimo("1234")

# Podemos ver y modificar las variables públicas libremente:
print(f"Este diario pertenece a: {mi_diario.dueño}")
mi_diario.dueño = "Batman"
print(f"Ahora el diario pertenece a: {mi_diario.dueño}")


print("--- 3. Intentando interactuar con la zona privada ---")

# Si le quitas el símbolo '#' a la siguiente línea, el programa explotará 
# con un AttributeError, porque '__secreto' es invisible desde afuera.
# print(mi_diario.__secreto)

# La forma correcta de interactuar es usando nuestros "botones" (métodos públicos)
print("\nIntento fallido:")
mi_diario.leer_secreto("0000")

print("\nIntento exitoso:")
mi_diario.leer_secreto("1234")
