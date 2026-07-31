# Traemos al cerebro (IA) y al pintor (Matplotlib)
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

print("--- 1. Los datos del mundo real ---")
# Preguntas: Horas estudiadas (¡doble corchete!)
horas = [[1], [2], [3], [4], [5]]
# Respuestas reales: Calificaciones en el examen
# Nota que no es perfecto: subir de 2 a 3 horas dio 15 puntos (40 a 55),
# pero subir de 3 a 4 horas dio 25 puntos (55 a 80). ¡La vida real es desordenada!
calificaciones_reales = [20, 40, 55, 80, 95]

print("\n--- 2. Entrenando a la IA ---")
cerebro = LinearRegression()
cerebro.fit(horas, calificaciones_reales)

print("\n--- 3. Extrayendo la línea perfecta ---")
# Para poder dibujar el "palo de escoba", le decimos a la IA:
# "Dime qué calificación PERFECTA habrías predicho para estas horas de estudio"
predicciones_perfectas = cerebro.predict(horas)

print("\n--- 4. Pintando la realidad y la predicción ---")
# 4.1 Dibujamos la vida real como puntos sueltos (Las canicas)
plt.scatter(horas, calificaciones_reales)

# 4.2 Dibujamos la predicción como una línea continua (El palo de escoba)
# Fíjate que usamos las 'predicciones_perfectas', NO las calificaciones reales
plt.plot(horas, predicciones_perfectas)

print("¡Abre los ojos! Verás cómo la línea intenta pasar justo por el medio de los puntos.")
# Revelamos la obra
plt.show()
