# Reto 39: El Tablero del Tesoro 🗺️

¡Eres un buscador de tesoros! Tienes un mapa de una playa dividida en cuadrantes. La playa está llena de `"arena"`, pero en algún lugar se encuentra el preciado `"tesoro"`. Tu misión es barrer toda la playa cuadrante por cuadrante hasta encontrarlo.

### Instrucciones paso a paso:
1. Crea una lista de listas (matriz) llamada `playa`. Debe tener 3 listas adentro. 
   - La primera lista debe ser: `["arena", "arena", "arena"]`
   - La segunda lista debe ser: `["arena", "tesoro", "arena"]`
   - La tercera lista debe ser: `["arena", "arena", "arena"]`
2. Imprime el mensaje: `"Iniciando escaneo de la playa..."`.
3. Crea tu **bucle exterior** para recorrer la `playa`. Usa la variable temporal `fila`.
4. **Dentro del bucle exterior** (primer nivel de indentación):
   - Imprime: `"Revisando nueva fila..."`.
   - Crea tu **bucle interior** para recorrer la `fila`. Usa la variable temporal `cuadrante`.
5. **Dentro del bucle interior** (segundo nivel de indentación):
   - Agrega un bloque `if` que compruebe si el `cuadrante` es exactamente igual (`==`) a `"tesoro"`.
   - Si es igual, imprime `"¡Tesoro encontrado! 💎"`.
   - Si no lo es (puedes usar un `if` que compruebe si es `"arena"` o simplemente usar tu imaginación, pero hazlo simple), no imprimas nada por la arena para no llenar la pantalla, SOLO busca el tesoro. *Opcional: imprime "Buscando..." en cada paso si lo deseas, pero para coincidir con la salida esperada, solo avisa cuando lo encuentres.*
6. **Fuera de todos los bucles**, imprime: `"Escaneo terminado."`.

### Reglas estrictas:
- **Conceptos permitidos**: Variables, textos (`""`), matrices (`[[]]`), bucles `for` anidados, condicionales `if`, igualdad (`==`), función `print`.
- **Prohibido**: Buscar el tesoro usando posiciones numéricas (`playa[1][1]`). Debes obligar a la computadora a recorrer todo el mapa con los dos bucles.

### Resultado esperado en la terminal:
```text
Iniciando escaneo de la playa...
Revisando nueva fila...
Revisando nueva fila...
¡Tesoro encontrado! 💎
Revisando nueva fila...
Escaneo terminado.
```
