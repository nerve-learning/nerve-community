# Reto 13: El Portero del Antro VIP 🕶️🕺

Acabas de conseguir trabajo como el cadenero (portero) del club más exclusivo de la ciudad. 
Tienes un escáner en tu puerta, y tu deber es dejar pasar a la gente **SOLO** si cumplen con los requisitos. A los que no, simplemente los ignoras (no hemos aprendido a decirles que no aún, lo haremos luego).

## Instrucciones

1. Crea dos variables para tu cliente en la fila:
   * `edad_cliente` (un número entero, ej. `20`).
   * `ropa_elegante` (un booleano `True` o `False`).

2. Crea tu condición `if`. El cliente solo entra si tiene 18 años o más, **y** además viene con `ropa_elegante` (`True`). 
   * Recuerda usar el comparador `>=` y el operador lógico `and` que vimos en niveles anteriores.
   * No olvides los dos puntos `:` al final.

3. Dentro del `if` (con sangría / 4 espacios hacia la derecha), imprime dos mensajes:
   * `"¡Bienvenido al club VIP!"`
   * `"Pasa a la zona de bebidas."`

4. Fuera del `if` (sin sangría, pegado a la izquierda), imprime siempre:
   * `"Siguiente en la fila, por favor..."`

### Conceptos permitidos
- Variables (asignación con `=`).
- Tipos de datos (`int`, `bool`).
- Operadores de comparación (`>=`, `==`).
- Operador lógico (`and`).
- La estructura `if` y la indentación.
- `print()`.

### Conceptos prohibidos
- `else` o `elif`. Si el cliente no cumple, simplemente se ignora y el código salta al "Siguiente en la fila...".
- Ciclos (`for`, `while`).
- Funciones `def`.

### Resultado esperado en terminal
Si configuras `edad_cliente = 20` y `ropa_elegante = True`, el resultado debe ser:

```text
¡Bienvenido al club VIP!
Pasa a la zona de bebidas.
Siguiente en la fila, por favor...
```

Si cambias los datos a `edad_cliente = 17` o `ropa_elegante = False`, el resultado debe ser **solamente**:

```text
Siguiente en la fila, por favor...
```
