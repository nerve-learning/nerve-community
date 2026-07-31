# Nivel 45: Secretos y Megáfonos (El Scope) 🕵️‍♂️

Imagina que estás en tu habitación (una función). Si susurras un secreto, solo tú y los que están en la habitación lo saben. Pero si tu mamá grita desde el pasillo principal de la casa (fuera de las funciones), todos en todas las habitaciones pueden escucharla.

En programación, las variables (las cajas donde guardamos datos) tienen un **tiempo de vida** y una **visibilidad**. A esto se le llama **Scope** (o ámbito).

Hasta ahora hemos creado variables sin pensar mucho dónde viven. Pero cuando usamos funciones, las reglas cambian:
1. **Variables Locales (El Secreto):** Nacen dentro de una función y mueren cuando la función termina. El resto del código no sabe que existen.
2. **Variables Globales (El Megáfono):** Nacen en el código principal (afuera de las funciones) y cualquier función puede verlas.

## 🗺️ Ruta de Aprendizaje
1. **Teoría:** Aprenderemos la regla de Las Vegas ("lo que pasa en la función, se queda en la función") y conoceremos la palabra mágica `global`.
2. **Ejemplo:** Jugaremos con la puntuación de un juego para ver cómo las funciones pueden modificar una variable de todo el sistema.
3. **Reto:** Construirás un sistema bancario o de monedas para un personaje que interactúa con múltiples funciones.

¡Es hora de entender dónde viven y mueren tus datos!
