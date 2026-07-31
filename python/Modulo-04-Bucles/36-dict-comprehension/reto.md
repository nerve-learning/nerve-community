# Reto 36: El Traductor Alienígena 👽

¡Has hecho contacto con una nave alienígena! Han aprendido algunas palabras de nuestro idioma, pero para que su computadora las entienda, deben tener la terminación `"-ZORK"`. Tu misión es construir el diccionario traductor que su computadora necesita.

### Instrucciones paso a paso:
1. Crea una lista llamada `humanos` que contenga las siguientes palabras (cadenas): `"paz"`, `"amor"`, `"vida"`.
2. Escribe en pantalla: `"Iniciando sistema de traducción..."`.
3. Crea una variable llamada `traductor`.
4. Asigna a `traductor` una **Comprensión de Diccionario** (`{}`) que haga lo siguiente:
   - Toma cada `palabra` (variable temporal) de la lista `humanos`.
   - La **llave** de tu diccionario debe ser la variable `palabra` intacta.
   - Usa los dos puntos `:` para separar.
   - El **valor** debe ser la variable `palabra` sumada (concatenada) con el texto `"-ZORK"`.
5. Por último, imprime en pantalla la variable `traductor`.

### Reglas estrictas:
- **Conceptos permitidos**: Variables, listas de textos (`[]`), llaves para diccionarios (`{}`), suma de textos (`+`), función `print`, y la sintaxis de comprensión de diccionarios (`{llave: valor for elemento in lista}`).
- **Prohibido**: Escribir el diccionario final a mano (es decir, no puedes hacer `{"paz": "paz-ZORK", ...}`). No puedes usar bucles `for` tradicionales de múltiples líneas.

### Resultado esperado en la terminal:
```text
Iniciando sistema de traducción...
{'paz': 'paz-ZORK', 'amor': 'amor-ZORK', 'vida': 'vida-ZORK'}
```
