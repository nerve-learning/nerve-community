# Nivel 76: Métodos de Clase y la Fábrica 🏭

Hasta ahora, todo lo que hemos programado vive en su propia burbuja. Un objeto de la clase `Perro` no tiene idea de cuántos otros perros has creado en tu programa. Su variable `self` solo guarda sus propios datos (su propio color, su propio nombre).

Pero, ¿qué pasa si queremos guardar información global? ¿Qué pasa si queremos saber **cuántos perros hemos creado en total**? No tiene sentido preguntárselo a un perro específico, deberíamos preguntárselo al "Molde" (a la Clase misma).

Aquí entran en juego las **Variables de Clase** y los **Métodos de Clase**. Son herramientas que nos permiten darle memoria y acciones a la Fábrica entera, en lugar de dárselas a los productos individuales.

## Ruta de aprendizaje
1. **Teoría (`teoria.md`)**: Entenderemos la diferencia entre `self` (el producto) y `cls` (la fábrica).
2. **Ejemplo (`ejemplo.py`)**: Construiremos una fábrica de robots que lleva un conteo estricto de su producción.
3. **Reto (`reto.md`)**: Serás el gerente de una Pizzería y tendrás que reportar las ventas totales. ¡A programar!
