# Reto 85: El Oráculo del Helado

Eres el dueño de una heladería y te has dado cuenta de que el clima afecta directamente a tus ventas. 
Has anotado tus datos del pasado:
- Cuando hace **10** grados, vendes **20** helados.
- Cuando hace **20** grados, vendes **40** helados.
- Cuando hace **30** grados, vendes **60** helados.

Acabas de ver las noticias y mañana habrá una ola de calor histórico: **40** grados. Necesitas que una IA prediga cuántos helados vas a vender para saber si debes comprar más ingredientes.

### Pasos a seguir:
1. Trae a la clase `LinearRegression` desde `sklearn.linear_model`.
2. Crea una variable `grados_pasado` con las temperaturas (¡recuerda los dobles corchetes! `[[10], [20], ...]`).
3. Crea una variable `ventas_pasado` con los helados vendidos (lista normal).
4. Crea un objeto IA ejecutando `LinearRegression()` y guárdalo en una variable.
5. Usa `.fit()` para que tu IA estudie los grados y las ventas del pasado.
6. Usa `.predict()` para preguntarle qué pasará si hacen `[[40]]` grados. Guarda la respuesta.
7. Imprime la respuesta en la terminal.

### Reglas estrictas:
- **PERMITIDO:** `from sklearn.linear_model import LinearRegression`, instanciar la clase, `fit()`, `predict()`, listas `[]`, listas anidadas `[[]]`, `print()`.
- **PROHIBIDO:** Usar Numpy o Pandas, resolver el problema mentalmente y hacer un `print(80)`. La IA tiene que aprenderlo sola.

### Resultado esperado en la terminal:
*(Nota: la IA devuelve el resultado envuelto en una lista, es normal)*
```text
[80.]
```
