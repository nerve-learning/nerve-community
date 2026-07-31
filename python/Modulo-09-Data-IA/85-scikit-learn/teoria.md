# Teoría: Entrenando al Cerebro

Para hacer Machine Learning, vamos a traer a un "alumno" especializado de la librería `sklearn` (el apodo de código para Scikit-Learn). 

Hoy usaremos un alumno llamado `LinearRegression` (Regresión Lineal). Su única especialidad en la vida es trazar líneas invisibles para descubrir cómo una cosa afecta a otra (por ejemplo, cómo los años de experiencia afectan tu sueldo).

## Anatomía del Aprendizaje

```python
from sklearn.linear_model import LinearRegression
```
- **`from ... import`**: "Del salón de clases de modelos lineales, tráeme al alumno `LinearRegression`".

```python
cerebro = LinearRegression()
```
- ¿Recuerdas la Programación Orientada a Objetos (Nivel 71)? Aquí estamos **instanciando** un objeto. Creamos un cerebro nuevo y vacío.

```python
cerebro.fit(preguntas, respuestas)
```
- **`fit`**: Significa "ajustar" o "entrenar". Aquí encerramos al cerebro en la biblioteca. Le damos las `preguntas` (ej: tamaño de casa) y las `respuestas` correctas del pasado (ej: precio). Él estudiará hasta encontrar la regla matemática que las conecta.

```python
resultado = cerebro.predict(nueva_pregunta)
```
- **`predict`**: Significa "predecir". Es el examen final. Le hacemos una pregunta que nunca ha visto y él usará lo que aprendió en el paso anterior para darnos su mejor suposición.

## ¿Qué pasa si me equivoco?

### El error de los dobles corchetes (Expected 2D array)
**El error:** 
```python
preguntas = [1, 2, 3] # Lista normal
cerebro.fit(preguntas, respuestas)
```
La terminal explotará gritando: `ValueError: Expected 2D array, got 1D array instead`.

**¿Por qué?** Scikit-Learn es extremadamente exigente con la forma de las preguntas. Te obliga a meter cada pregunta dentro de su propia lista individual: `[[1], [2], [3]]`. 
Hace esto porque en el mundo real, una pregunta podría tener muchas variables (ej: `[[1_habitacion, 2_baños], [3_habitaciones, 1_baño]]`). Aunque hoy solo usemos una variable, él sigue exigiendo la estructura de lista de listas (doble corchete).
**La solución:** Siempre pon tus datos de entrada (las preguntas/eje X) como listas dentro de listas: `[[1], [2], [3]]`. Las respuestas (eje Y) sí van en una lista normal `[100, 200, 300]`.
