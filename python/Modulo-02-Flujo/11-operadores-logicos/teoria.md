# Teoría: El arte de combinar condiciones

Hasta hoy sabemos comparar datos para obtener `True` (Verdad) o `False` (Mentira), por ejemplo: `edad >= 18`. Pero, ¿qué hacemos si necesitamos que se cumplan múltiples cosas a la vez?

Aquí entran los tres operadores lógicos de Python. Estas palabras mágicas siempre conectan o modifican valores que son `True` o `False`.

### 1. El guardia estricto: `and` (Y)
El operador `and` une dos condiciones. Para que el resultado final sea `True`, **AMBAS** condiciones deben ser verdad. Si una sola falla, todo se derrumba y el resultado es `False`.

* **Analogía**: ¿Me prestas tu celular? Solo si "Lavaste los platos" `and` "Hiciste la tarea". Si fallas en una, la respuesta es no.

### 2. El guardia relajado: `or` (O)
El operador `or` es súper comprensivo. Con que **AL MENOS UNA** de las condiciones sea verdad, él dará un `True`. Solo dará `False` si absolutamente todas las condiciones son mentira.

* **Analogía**: Para pagar en el supermercado, puedes usar "Efectivo" `or` "Tarjeta". Si traes cualquiera de los dos, puedes pagar. Solo si no traes ninguno, no puedes comprar.

### 3. El rebelde contreras: `not` (NO)
El operador `not` no une dos cosas, solo necesita una. Lo único que hace es voltear la moneda. Si algo era `True`, lo vuelve `False`. Si era `False`, lo vuelve `True`.

* **Analogía**: Hoy es domingo (día de descanso). Si pregunto `not` (no es) día de descanso, la respuesta será "Falso".

---

## Anatomía (Sintaxis)

```python
condicion_1 and condicion_2
```
* `condicion_1`: Algo que resulta en `True` o `False` (ej. `edad > 18`).
* `and`: La palabra mágica reservada por Python, siempre en minúsculas y rodeada de espacios. Une lo de la izquierda con lo de la derecha.
* `condicion_2`: La segunda regla a evaluar.

```python
not condicion
```
* `not`: Va *antes* de lo que queremos voltear.

---

## ¿Qué pasa si me equivoco?

**El error del "lenguaje humano"**
A veces intentamos hablarle a Python como le hablamos a un amigo:
`color == "rojo" or "azul"`

Si escribes esto, la computadora se va a confundir horriblemente. Para Python, el `or` corta la frase en dos universos aislados. 
Universo 1: `color == "rojo"`
Universo 2: `"azul"`
Python creerá que la palabra `"azul"` por sí sola es un `True` gigante porque es texto que existe. 

**La forma correcta (y obligatoria para ti):** 
Debes hacer la comparación completa en cada lado del `or`:
`color == "rojo" or color == "azul"`
