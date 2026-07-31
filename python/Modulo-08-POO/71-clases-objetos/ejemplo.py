# Usaremos 'class' para definir nuestro molde. 
# Nota: La primera letra en mayúscula (Robot) es una regla de etiqueta de los programadores.

print("--- 1. Creando nuestro molde (La Clase) ---")

class Robot:
    # __init__ es el paso de "preparación" de nuestro robot en la fábrica.
    # self es el robot mismo. Le permite al robot guardar sus propios datos.
    def __init__(self, nombre_asignado, color_asignado):
        # Usamos el punto (.) para guardar los datos DENTRO de este robot en específico.
        # Es como decirle: "Tu propio nombre (self.nombre) será igual a lo que me acaban de pasar".
        self.nombre = nombre_asignado
        self.color = color_asignado

    # Podemos darle habilidades (funciones) al molde.
    # Siempre deben llevar 'self' primero en los paréntesis, para saber qué robot está hablando.
    def saludar(self):
        # Gracias a 'self', el robot sabe buscar su propio nombre y color.
        print(f"¡Bip bop! Soy {self.nombre} y mi armadura es {self.color}.")


print("--- 2. Construyendo robots reales (Los Objetos) ---")

# Ahora usamos el molde para crear dos robots distintos.
# Los paréntesis () en Robot(...) le dicen a Python: "Ve a buscar el __init__ y enciende la fábrica".
# NOTA: Python asigna 'self' automáticamente al objeto que se está creando.
# Nosotros solo pasamos el segundo y tercer parámetro (nombre_asignado y color_asignado).
robot_uno = Robot("R2-D2", "Blanca y Azul")
robot_dos = Robot("Wall-E", "Amarilla oxidada")


print("--- 3. Usando nuestros robots ---")

# Usamos el punto (.) para decirle a un robot específico que ejecute su acción.
robot_uno.saludar()
robot_dos.saludar()


print("--- 4. Viendo sus datos por dentro ---")

# También podemos usar el punto (.) para espiar los datos que el robot guardó en su 'self'.
print(f"El color secreto del segundo robot es: {robot_dos.color}")
