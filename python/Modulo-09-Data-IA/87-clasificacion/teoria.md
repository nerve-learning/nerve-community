# Teoría: El Juego de las 20 Preguntas

Imagina el juego donde tienes que adivinar un personaje haciendo preguntas de "Sí" o "No". ¿Tiene pelo? Sí. ¿Ladra? No. ¿Maúlla? Sí. ¡Es un gato!

En Machine Learning, podemos crear una IA que haga exactamente eso. Se llama **Árbol de Decisiones** (`DecisionTreeClassifier`). Va creando caminos lógicos en su cerebro ("Si pesa más de 10 kilos, vete por la rama izquierda, entonces es un perro").

La maravilla de Scikit-Learn es que, sin importar si usamos el alumno que traza líneas (`LinearRegression`) o el alumno que hace preguntas (`DecisionTreeClassifier`), **las instrucciones son exactamente las mismas**.

## Anatomía del Clasificador

```python
from sklearn.tree import DecisionTreeClassifier
```
- **`from sklearn.tree`**: Del salón de los árboles lógicos de Scikit-Learn...
- **`import DecisionTreeClassifier`**: Trae al alumno "Clasificador por Árbol de Decisiones".

```python
cerebro = DecisionTreeClassifier()
cerebro.fit(pistas, etiquetas_reales)
prediccion = cerebro.predict(pistas_nuevas)
```
- ¡Es exactamente la misma sintaxis del Nivel 85! Instanciamos, entrenamos con `.fit()` y adivinamos con `.predict()`. 

## ¿Qué pasa si me equivoco?

### El error de confundir al alumno (Regresión vs Clasificación)
**El error:**
Intentar usar `LinearRegression` (del nivel 85) cuando tus respuestas son textos como `["Gato", "Perro"]`.
La terminal te dará un error gigante que dirá algo como: `ValueError: could not convert string to float: 'Gato'`

**¿Por qué?** `LinearRegression` es un matemático estricto. Solo sabe hacer cálculos con números. Si le entregas la palabra "Gato", su cerebro hace cortocircuito porque no sabe cómo multiplicar o sumar la letra "G".
**La solución:** Cuando tus respuestas (`y`) son **etiquetas o categorías** (palabras), SIEMPRE debes usar un Clasificador (como `DecisionTreeClassifier`). Cuando tus respuestas son **números continuos** (precios, temperaturas), usas Regresión.
