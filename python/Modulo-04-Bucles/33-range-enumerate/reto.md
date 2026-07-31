# Reto 33: El Eco de la Montaña 🏔️

¡Estás en la cima de una gran montaña! Quieres gritar la palabra "¡Hola!" y escuchar cómo el eco te la devuelve varias veces. Para saber qué eco es cuál, la montaña numera mágicamente cada repetición.

### Instrucciones paso a paso:
1. Escribe un mensaje en pantalla que anuncie tu grito: `"Gritando a la montaña..."`.
2. Utiliza un bucle `for` junto con la herramienta `range()` para generar exactamente **4 repeticiones**.
3. Usa la variable temporal `eco` para guardar el número que te entrega el `range`.
4. **Dentro del bucle** (con indentación):
   - Imprime la palabra `"¡Hola!"`.
   - Luego, imprime la variable `eco` para ver qué número de repetición te devolvió la montaña en ese instante.
5. **Fuera del bucle** (sin indentación), imprime: `"El eco se desvaneció."`.

### Reglas estrictas:
- **Conceptos permitidos**: Bucle `for`, palabra `in`, herramienta `range()`, paréntesis `()`, función `print`, variable temporal, dos puntos (`:`), indentación.
- **Prohibido**: No puedes usar listas (nada de corchetes `[]`), no puedes usar bucles `while`, y no puedes sumar texto con números (no uses `+` para unir `"¡Hola!"` y el número). Imprímelos en líneas separadas.

### Resultado esperado en la terminal:
```text
Gritando a la montaña...
¡Hola!
0
¡Hola!
1
¡Hola!
2
¡Hola!
3
El eco se desvaneció.
```
