# ==========================================
# NIVEL 03: LETRAS Y NÚMEROS
# ==========================================

print("--- Datos del Sistema ---")

# Esto es un TEXTO (String). Va con comillas.
# Es solo la palabra "Planeta".
categoria = "Planeta"

# Esto es un NÚMERO ENTERO (Integer). ¡Va sin comillas!
# Es una cantidad real matemática.
temperatura = 22

# Imprimimos ambos. 
# En la terminal, la computadora es muy educada y los muestra igual, 
# pero por dentro, sabe que uno es texto y el otro es cantidad.
print(categoria)
print(temperatura)

print("--- El engaño visual ---")

# Cuidado aquí: "2024" tiene comillas, así que para la máquina 
# esto es una PALABRA, igual que "Perro" o "Gato". ¡No es un número!
anio_texto = "2024"

# Esto SÍ es un número entero.
anio_numero = 2024

print("Ambos se ven igual en pantalla:")
print(anio_texto)
print(anio_numero)
# Pero recuerda: no puedes sumar el texto, solo el número.
