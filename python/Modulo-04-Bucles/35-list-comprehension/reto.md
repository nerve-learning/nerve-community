# Reto 35: La Panadería Exprés 🥖

Eres el dueño de una famosa panadería. Hoy la harina subió de precio, así que tienes que subir el precio de todos tus panes en **5 monedas** de oro. Tienes una lista larga de precios y no quieres hacerlo a mano. ¡Es hora de usar la máquina clonadora!

### Instrucciones paso a paso:
1. Crea una lista llamada `precios_viejos` con los números: `10`, `20`, `30`, `40`.
2. Escribe en pantalla: `"Actualizando precios en la caja registradora..."`.
3. Crea una variable llamada `precios_nuevos`.
4. Asigna a `precios_nuevos` una **Comprensión de Lista** (`[]`) que haga lo siguiente:
   - Toma cada `precio` (variable temporal) de la lista `precios_viejos`.
   - A cada `precio` súmale `5`.
5. Por último, imprime en pantalla la variable `precios_nuevos`.

### Reglas estrictas:
- **Conceptos permitidos**: Variables, listas de números (`[]`), suma matemática (`+`), función `print`, y la sintaxis de comprensión de listas (`[accion for elemento in lista]`).
- **Prohibido**: Escribir la lista final a mano (es decir, no puedes hacer `[15, 25, 35, 45]`). No puedes usar un bucle `for` tradicional con indentación de múltiples líneas. TODO el trabajo debe hacerse en una sola línea mágica.

### Resultado esperado en la terminal:
```text
Actualizando precios en la caja registradora...
[15, 25, 35, 45]
```
