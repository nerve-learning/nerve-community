# ---------------------------------------------------------
# Proyecto: Predictor de Aprobación Escolar
# Usaremos un Árbol de Decisión para predecir si un
# alumno pasa o reprueba el examen.
# ---------------------------------------------------------

# Importamos las herramientas (como sacar las ollas de la cocina)
from sklearn.tree import DecisionTreeClassifier

print("--- 1. Recolectando Datos ---")
# Datos históricos (nuestra experiencia del pasado)
# Cada lista interna es un alumno: [Horas de estudio, Horas de sueño]
caracteristicas = [
    [1, 8],  # Alumno 1: Estudió poco, durmió mucho
    [5, 7],  # Alumno 2: Estudió regular, durmió regular
    [8, 6],  # Alumno 3: Estudió mucho, durmió poco
    [0, 4]   # Alumno 4: No estudió, no durmió
]

# Resultados (0 = Reprobó, 1 = Aprobó)
# Cada resultado corresponde al alumno en la misma posición de arriba
resultados = [0, 1, 1, 0]
print("Datos listos. Tenemos 4 alumnos de ejemplo.")

print("\n--- 2. Entrenando el Modelo ---")
# Creamos el modelo (nuestro cerebro en blanco)
modelo = DecisionTreeClassifier()

# Le enseñamos usando .fit() (aprender)
modelo.fit(caracteristicas, resultados)
print("🧠 ¡El modelo ha aprendido los patrones matemáticos!")

print("\n--- 3. Haciendo Predicciones ---")
# Llega un alumno nuevo que estudió 3 horas y durmió 8
nuevo_alumno = [[3, 8]] # ¡Ojo! Lista dentro de lista

# Le pedimos al modelo que prediga (adivine)
prediccion = modelo.predict(nuevo_alumno)

print(f"El alumno nuevo estudió {nuevo_alumno[0][0]} horas y durmió {nuevo_alumno[0][1]} horas.")

# La predicción viene en una lista, así que sacamos el primer elemento con [0]
if prediccion[0] == 1:
    print("🔮 Predicción: ¡Este alumno va a APROBAR! 🎉")
else:
    print("🔮 Predicción: Este alumno va a REPROBAR. 😢")
