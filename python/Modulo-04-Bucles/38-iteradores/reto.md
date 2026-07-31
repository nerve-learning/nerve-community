# Reto 38: El Repartidor de Cartas 🃏

¡Eres un crupier en un casino! Tienes una baraja especial de cartas en tu mano. El juego consiste en sacar solo las primeras **dos** cartas, una por una, y anunciarlas en la mesa. Las demás cartas se quedan en la baraja para la siguiente ronda.

### Instrucciones paso a paso:
1. Crea una lista llamada `baraja` con las siguientes 3 cartas (textos): `"As de Corazones"`, `"Rey de Espadas"`, `"Reina de Tréboles"`.
2. Convierte tu `baraja` en una máquina de turnos usando `iter()`. Guarda esa máquina en una nueva variable llamada `repartidor`.
3. Imprime el mensaje: `"¡Comienza el juego!"`.
4. Usa la herramienta `next()` con tu `repartidor` para sacar la **primera** carta. Guarda esa carta en una variable llamada `carta1`.
5. Imprime el mensaje `"Primera carta:"` y luego imprime la variable `carta1`.
6. Usa la herramienta `next()` con tu `repartidor` OTRA VEZ para sacar la **segunda** carta. Guárdala en una variable llamada `carta2`.
7. Imprime el mensaje `"Segunda carta:"` y luego imprime la variable `carta2`.
8. Imprime el mensaje: `"La última carta se queda oculta."`

### Reglas estrictas:
- **Conceptos permitidos**: Variables, listas de textos (`[]`), funciones `iter()`, `next()` y `print`.
- **Prohibido**: No puedes usar bucles `for` ni `while`. No puedes sacar elementos usando su posición numérica (prohibido hacer `baraja[0]`). Tienes que hacerlo jalando la palanca `next()`.

### Resultado esperado en la terminal:
```text
¡Comienza el juego!
Primera carta:
As de Corazones
Segunda carta:
Rey de Espadas
La última carta se queda oculta.
```
