# ¡REGLA DE ORO! Todos los imports van en las primeras líneas.
import math
from random import choice


print("--- 1. Usando la caja completa (math) ---")

# math tiene herramientas geniales para matemáticas
numero = 16

# Usamos la sintaxis: caja.herramienta()
raiz_cuadrada = math.sqrt(numero)
# math.pow(base, exponente) eleva a una potencia
potencia = math.pow(2, 3) # 2 al cubo (8)

print("La raíz de 16 es:", raiz_cuadrada)
print("2 elevado a 3 es:", potencia)


print("\n--- 2. Usando una herramienta suelta (random.choice) ---")

# La herramienta 'choice' elige un elemento al azar de una lista.
# Fíjate que como hicimos "from random import choice", 
# NO tenemos que escribir "random.choice", la usamos directamente.

heroes = ["Mago", "Guerrero", "Arquero", "Ladrón"]

print("Eligiendo tu clase al azar...")
clase_elegida = choice(heroes)
print("¡Felicidades, jugarás como:", clase_elegida, "!")

# Si ejecutamos esto de nuevo, la suerte cambiará
print("Tirando los dados otra vez, jugarás como:", choice(heroes))


print("\n--- 3. ¿Podemos crear nuestras propias herramientas? ---")
# La respuesta es SÍ. Un archivo .py que tú creas (como 'ejemplo.py') 
# ES una caja de herramientas.
# En el futuro aprenderemos a tener múltiples archivos para que un archivo
# importe las funciones que creaste en otro. ¡Esa es la base de los sistemas enormes!
