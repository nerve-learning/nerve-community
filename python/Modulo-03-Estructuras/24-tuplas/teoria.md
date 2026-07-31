# Teoría: La anatomía de una Tupla

Para crear una Tupla (nuestra caja fuerte), usamos **los paréntesis `(` y `)`** en lugar de los corchetes `[` y `]`.

Todo lo demás funciona exactamente igual que las listas: separamos los elementos con comas `,` y podemos acceder a ellos usando el índice (como `tupla[0]`).

## Anatomía

```python
dias_semana = ("Lunes", "Martes", "Miércoles")
```

Desmontemos la sintaxis:
- `dias_semana`: El nombre de nuestra variable.
- `=`: El símbolo de asignación (guardar en la variable).
- `(`: Abre la caja fuerte. Significa "aquí empieza una tupla".
- `"Lunes", "Martes", "Miércoles"`: Los elementos separados por comas.
- `)`: Cierra y **sella** la caja fuerte.

## El Superpoder: Inmutabilidad
"Inmutable" es una palabra elegante para decir "no se puede cambiar". 
Como la tupla está sellada, **NO** puedes usar `.append()` ni `.remove()`. Tampoco puedes cambiar el valor de un compartimento.

## ¿Qué pasa si me equivoco?

**El error más común:** Intentar modificar la tupla.
Si olvidas que estás usando una tupla (paréntesis) e intentas cambiarla como si fuera una lista:
```python
mis_numeros = (1, 2, 3)
mis_numeros.append(4)
```
La terminal se pondrá roja como una sirena y mostrará: `AttributeError: 'tuple' object has no attribute 'append'`. 
Traducción humana: "¡Oye, las tuplas no tienen el botón de agregar! ¡Están selladas!".
