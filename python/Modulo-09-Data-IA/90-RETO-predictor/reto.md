# Reto 90: El Tasador de Casas Automático 🏠

¡Bienvenido a tu prueba final del módulo de Datos e IA!

Acabas de ser contratado por una inmobiliaria prestigiosa. Quieren que construyas un programa inteligente que pueda adivinar el precio de una casa basándose únicamente en su tamaño.

## Instrucciones

1. Importa la herramienta `LinearRegression` de la librería `sklearn.linear_model`. (Usamos regresión lineal porque queremos predecir un número continuo, no una categoría).
2. Crea tus datos de entrenamiento (el pasado):
   - Crea una variable `tamaños` que sea una lista de listas con los metros cuadrados: `50`, `80`, `100`, `150`.
   - Crea una variable `precios` que sea una lista simple con los precios en miles de dólares: `100`, `160`, `200`, `300`.
3. Crea tu modelo de regresión lineal.
4. Entrénalo pasándole los `tamaños` y los `precios` usando `.fit()`. Imprime un mensaje indicando que está entrenando.
5. Llega un cliente nuevo con una casa de **120** metros cuadrados. 
6. Usa `.predict()` pasándole el `[[120]]` para calcular en cuánto debería venderla.
7. Guarda el resultado en una variable e imprímela con un mensaje amigable.

### Conceptos permitidos:
- Importar módulos (`from ... import ...`)
- Listas y Listas dentro de Listas (`[]`)
- Modelos de `scikit-learn` (`LinearRegression`, `.fit()`, `.predict()`)
- `print()`

### Conceptos prohibidos:
- Copiar y pegar el código del ejemplo. ¡Escríbelo tú mismo desde cero para que tu cerebro construya las conexiones!
- Usar datos diferentes a los que te di.

### Resultado esperado en la terminal:
*(El número exacto puede variar un poquitito por los decimales, pero debe ser 240.0)*
```text
Entrenando al tasador automático...
¡Entrenamiento completado!
Calculando precio para una casa de 120 metros cuadrados...
🔮 El precio sugerido es: $240.0 miles de dólares.
```
