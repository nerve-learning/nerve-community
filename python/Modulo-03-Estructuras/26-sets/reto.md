# Reto 26: La Colección de Estampas 🃏

Estás coleccionando estampas (cromos/cartas) de tus personajes favoritos. Cuando compraste un paquete nuevo, te salieron algunas estampas repetidas. ¡Necesitas organizar tu colección para saber exactamente cuántas estampas ÚNICAS tienes!

## Instrucciones

1. Crea un archivo llamado `reto.py`.
2. Crea una variable llamada `mis_estampas` que sea un **Set** (usando llaves `{}`).
3. Dentro del Set, escribe estos nombres exactamente, ¡con todo y repetidos!:
   `"Batman"`, `"Spiderman"`, `"Batman"`, `"Superman"`, `"Spiderman"`
4. Imprime el mensaje: `"Mi colección sin repetidas:"`.
5. Imprime tu Set `mis_estampas`. (Verás que Python eliminó a los clones por ti).
6. Te acaban de regalar una nueva estampa. Usa el método `.add()` para agregar `"Wonder Woman"` a tu colección.
7. Imprime el mensaje: `"Nueva colección:"` y vuelve a imprimir tu Set.

### Conceptos Permitidos
- Sets (creación con llaves `{}`).
- El método `.add("elemento")` para agregar.
- La función `print()`.

### Conceptos PROHIBIDOS
- Usar corchetes `[]` para crear la colección (eso haría que fuera una Lista, ¡y guardaría los repetidos!).
- Intentar leer una estampa usando posiciones numéricas (`mis_estampas[0]`).
- Usar el método `.append()` (ese solo funciona en Listas, en Sets es `.add()`).

## Resultado Esperado en la Terminal

Al ejecutar tu código, la terminal debería mostrar EXACTAMENTE esto (¡Ojo! El orden de las palabras puede salir revuelto en tu pantalla, ¡y eso es normal en los Sets!):

```text
Mi colección sin repetidas:
{'Batman', 'Superman', 'Spiderman'}
Nueva colección:
{'Batman', 'Superman', 'Spiderman', 'Wonder Woman'}
```

¡Excelente trabajo organizando tu colección!
