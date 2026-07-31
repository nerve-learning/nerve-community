# Reto 37: El Chef Ensamblador 🍔

¡Trabajas en la cocina de un restaurante de comida rápida! Tienes dos bandas transportadoras. Por la izquierda llegan los tipos de pan, y por la derecha llegan los tipos de carne. Tu trabajo es usar la cremallera mágica para ensamblar la hamburguesa y anunciarla a los clientes.

### Instrucciones paso a paso:
1. Crea una lista llamada `panes` con estos tres textos: `"blanco"`, `"integral"`, `"con ajonjolí"`.
2. Crea una lista llamada `carnes` con estos tres textos: `"res"`, `"pollo"`, `"vegetariana"`.
3. Escribe un mensaje en pantalla que diga: `"¡Ensamblando pedidos!"`.
4. Crea un bucle `for` que use la herramienta `zip()` para unir la lista de `panes` con la lista de `carnes`.
5. Asegúrate de inventar y colocar **dos variables temporales** (por ejemplo: `tipo_pan` y `tipo_carne`) separadas por una coma.
6. **Dentro del bucle** (con indentación):
   - Imprime el mensaje `"Hamburguesa lista de:"`.
   - Imprime la variable de la carne.
   - Imprime el texto `"en pan"`.
   - Imprime la variable del pan.
7. **Fuera del bucle**, imprime `"¡Todos los pedidos entregados!"`.

### Reglas estrictas:
- **Conceptos permitidos**: Listas (`[]`), cadenas de texto (`""`), bucle `for`, palabra `in`, variables temporales, coma (`,`), herramienta `zip()`, función `print`, dos puntos (`:`), indentación.
- **Prohibido**: Prohibido usar contadores matemáticos, bucles `while`, o intentar buscar los elementos por su número de posición en la lista (no uses trucos que no hemos visto).

### Resultado esperado en la terminal:
```text
¡Ensamblando pedidos!
Hamburguesa lista de:
res
en pan
blanco
Hamburguesa lista de:
pollo
en pan
integral
Hamburguesa lista de:
vegetariana
en pan
con ajonjolí
¡Todos los pedidos entregados!
```
