# Traemos a nuestro nuevo alumno experto en poner etiquetas
from sklearn.tree import DecisionTreeClassifier

print("--- 1. Preparando las pistas y las etiquetas ---")
# Preguntas (X): [Peso en kilos, Altura en cm]
# Al igual que antes, usamos listas dentro de listas (dobles corchetes)
# Solo que ahora cada pregunta tiene DOS datos en lugar de uno.
caracteristicas_animales = [
    [4, 25],   # Pesa 4kg, mide 25cm
    [5, 30],   # Pesa 5kg, mide 30cm
    [30, 60],  # Pesa 30kg, mide 60cm
    [40, 70]   # Pesa 40kg, mide 70cm
]

# Respuestas (y): La etiqueta que le corresponde a cada animal de arriba
etiquetas_reales = ["Gato", "Gato", "Perro", "Perro"]

print("Datos de la veterinaria listos.")


print("\n--- 2. Entrenando a la IA ---")
# Creamos a nuestro cerebro clasificador
cerebro = DecisionTreeClassifier()

# Le pedimos que estudie los datos y encuentre la regla para diferenciar
cerebro.fit(caracteristicas_animales, etiquetas_reales)
print("¡La IA ha aprendido a diferenciar perros de gatos!")


print("\n--- 3. Adivinando lo desconocido ---")
# Nos traen un animal misterioso envuelto en una cobija.
# Lo pesamos y medimos: Pesa 35kg y mide 65cm.
# ¿Qué etiqueta le pondrá la IA? (OJO: Doble corchete)
animal_misterioso = [[35, 65]]

prediccion = cerebro.predict(animal_misterioso)

# Nos devolverá la etiqueta adivinada dentro de una lista
print("Según las medidas, la IA dice que el animal misterioso es un:")
print(prediccion)
