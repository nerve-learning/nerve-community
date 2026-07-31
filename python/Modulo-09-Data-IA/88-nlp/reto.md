# Reto 88: El Analista de Reseñas

Eres dueño de un restaurante famoso. Has recopilado 3 reseñas de internet y quieres preparar estos textos para que, en el futuro, una IA (como el Clasificador que hicimos en el nivel anterior) pueda leerlos y decirte si son comentarios positivos o negativos. 

Tus 3 reseñas son:
1. `"La comida es excelente"`
2. `"La comida es terrible"`
3. `"Excelente servicio"`

### Pasos a seguir:
1. Trae a la clase `CountVectorizer` desde `sklearn.feature_extraction.text`.
2. Crea una variable llamada `resenas` que sea una lista conteniendo exactamente esos 3 textos.
3. Crea a tu traductor `CountVectorizer()` y guárdalo en una variable.
4. Usa `.fit_transform()` pasándole tus reseñas, y guarda el resultado en una variable llamada `matriz_numeros`.
5. Imprime en pantalla la matriz. **¡Cuidado!** Recuerda agregar `.toarray()` o la computadora te devolverá un formato comprimido indescifrable.

### Reglas estrictas:
- **PERMITIDO:** `CountVectorizer`, `fit_transform()`, `toarray()`, listas y `print()`.
- **PROHIBIDO:** Contar las palabras mentalmente y crear la matriz a mano. Usar bucles `for`.

### Resultado esperado en la terminal:
Verás una matriz de 3 filas. Cada fila representa una de tus reseñas convertida en números (conteos de palabras).
```text
[[1 1 1 0 0 1]
 [0 1 0 1 1 0]
 [0 0 1 0 0 1]]
```
