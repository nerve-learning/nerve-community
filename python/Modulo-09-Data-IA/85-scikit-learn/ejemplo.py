# Importamos a nuestro modelo experto en trazar líneas lógicas
from sklearn.linear_model import LinearRegression

print("--- 1. Preparando los libros de estudio ---")
# Preguntas (X): Cuántas habitaciones tiene la casa.
# RECUERDA EL ERROR COMÚN: Tienen que ser listas dentro de listas.
habitaciones = [[1], [2], [3]]

# Respuestas (y): Cuánto costaron esas casas en miles de dólares.
# Estas sí van en una lista normal.
precios = [100, 200, 300]
print("Datos históricos listos.")


print("\n--- 2. Entrenando a la IA ---")
# Creamos a nuestro alumno vacío
mi_ia = LinearRegression()

# Le ordenamos estudiar (.fit)
print("La IA está estudiando los libros...")
mi_ia.fit(habitaciones, precios)
print("¡Listo! La IA ha descubierto la regla matemática oculta.")


print("\n--- 3. Prediciendo el futuro ---")
# Le hacemos una pregunta que NUNCA ha visto en sus datos originales.
# ¿Cuánto costará una casa de 5 habitaciones?
# OJO: La pregunta nueva también va entre dobles corchetes
casa_nueva = [[5]]

# Le pedimos que haga la predicción
prediccion = mi_ia.predict(casa_nueva)

print("Si la casa tiene 5 habitaciones, la IA predice que costará:")
# Nos devolverá una lista con la respuesta
print(prediccion)
