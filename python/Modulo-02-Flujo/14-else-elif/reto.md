# Reto 14: El Calificador de Exámenes 📝🎓

Tu maestro de programación te pidió ayuda para automatizar el sistema de calificaciones. Quieren dejar de usar números y pasar al sistema de letras (A, B, C, D, F).

Tu trabajo es escribir un código que tome una calificación numérica y, usando `if`, `elif` y `else`, decida qué letra imprimir en la terminal.

## Instrucciones

1. Crea una variable llamada `calificacion_examen` y ponle un número del 0 al 100 (ej. `85`).

2. Crea la estructura de decisiones usando este orden estricto de reglas:
   * Si la calificación es **mayor o igual a 90**, imprime `"Obtuviste una A. ¡Excelente!"`
   * Pero si en cambio es **mayor o igual a 80**, imprime `"Obtuviste una B. ¡Muy bien!"`
   * Pero si en cambio es **mayor o igual a 70**, imprime `"Obtuviste una C. ¡Aprobaste!"`
   * Pero si en cambio es **mayor o igual a 60**, imprime `"Obtuviste una D. ¡De panzazo!"`
   * Si nada de lo anterior funcionó (de lo contrario), imprime `"Obtuviste una F. Nos vemos en recursamiento."`

3. Recuerda cómo Python evalúa esto: de arriba hacia abajo. En el momento en que una condición sea cierta, ignorará todo lo demás.

### Conceptos permitidos
- Variables (asignación con `=`).
- Tipos de datos (`int`).
- Operadores de comparación (`>=`).
- Estructura condicional completa (`if`, `elif`, `else`).
- Indentación correcta.
- `print()`.

### Conceptos prohibidos
- El operador `and`. No lo necesitas. Gracias a que el `elif` solo se ejecuta si el de arriba falló, no tienes que comprobar rangos cerrados como "mayor a 80 y menor a 90".
- Ciclos (`for`, `while`).
- Funciones `def`.

### Resultado esperado en terminal
Si usas `calificacion_examen = 85`, al correr tu código la terminal debe mostrar exactamente esto:

```text
Obtuviste una B. ¡Muy bien!
```

Si luego lo cambias a `calificacion_examen = 55`, debe mostrar:

```text
Obtuviste una F. Nos vemos en recursamiento.
```
