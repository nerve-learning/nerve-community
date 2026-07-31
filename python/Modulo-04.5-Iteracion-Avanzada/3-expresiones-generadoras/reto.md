# Reto 3: El Cajero Nocturno 🏪

La tienda de la esquina cerró y el dueño quiere saber cómo le fue hoy. Tienes el registro de todas las ventas del día. Tu tarea: calcular varias estadísticas usando **expresiones generadoras** directamente dentro de `sum()` y `max()`, sin crear listas intermedias.

## Instrucciones Paso a Paso:

Copia este registro de ventas en tu código:

```python
ventas = [
    {"producto": "Refresco",  "precio": 18,  "cantidad": 12},
    {"producto": "Pan",       "precio": 22,  "cantidad": 30},
    {"producto": "Leche",     "precio": 25,  "cantidad": 8},
    {"producto": "Chicles",   "precio": 5,   "cantidad": 40},
    {"producto": "Jabón",     "precio": 38,  "cantidad": 5},
    {"producto": "Agua",      "precio": 12,  "cantidad": 20},
    {"producto": "Galletas",  "precio": 32,  "cantidad": 15},
]
```

Recuerda: cada venta es un diccionario. Para acceder al precio de una venta usa `venta["precio"]`, y para la cantidad `venta["cantidad"]`.

1. Calcula el **total de ingresos** del día. El ingreso de cada producto es `precio * cantidad`. Usa `sum()` con una expresión generadora.
2. Calcula el **ingreso máximo de un solo producto** (el que más dinero generó). Usa `max()` con una expresión generadora.
3. Cuenta **cuántos productos tienen precio mayor a 20 pesos**. Para esto, en lugar de `sum(precio...)`, haz `sum(1 for ...)` — suma un `1` por cada producto que cumpla la condición.
4. Imprime los tres resultados con el formato del resultado esperado.

> **Pista:** Dentro del generador, el cálculo `venta["precio"] * venta["cantidad"]` produce el ingreso de ese producto. Mete este cálculo como la "acción" del generador.

## Reglas Estrictas:
✅ **Conceptos Permitidos:** Expresiones generadoras `(...)`, `sum()`, `max()`, `for`, `if`, diccionarios `{}` y `[]` para acceder a claves, `print()`, f-strings.
❌ **Conceptos Prohibidos:** List comprehensions `[...]` como paso intermedio, crear listas temporales, `def` con `yield` (este reto es solo expresiones en línea).

## Resultado Esperado en tu Terminal:

```text
=== Reporte Nocturno de la Tienda ===

Total de ingresos del día:         $2,431
Producto que más ingresó:          $960 (Pan: 22 x 30)
Productos con precio mayor a $20:  4
```

Crea tu código en `reto.py`. Si puedes calcular las tres estadísticas en tres líneas de código (una por estadística), vas por el camino correcto.
