# ==========================================
# Archivo: ejemplo.py
# Autor: Kaia / Alenia Studios
# Descripción: Comprendiendo las Dict Comprehensions
# ==========================================

print("--- Clase de Magia ---")

# Tenemos la lista de los alumnos inscritos en la clase.
alumnos = ["Harry", "Hermione", "Ron"]

print("Alumnos en la lista:")
print(alumnos)

print("--- Tomando Asistencia Automática ---")

# Vamos a crear un NUEVO DICCIONARIO usando la etiquetadora mágica.
# La LLAVE será el nombre del alumno (la variable 'estudiante').
# El VALOR será el texto "Presente".
# El MOTOR es: for estudiante in alumnos

registro = {estudiante: "Presente" for estudiante in alumnos}

# ¡Eso es todo! Hemos creado un diccionario completo en una línea.
# Para "Harry", se creó el cajón "Harry" con el valor "Presente".
# Y así para todos los demás.

print("Registro de asistencia creado:")
print(registro)

print("--- Fin de la Clase ---")
