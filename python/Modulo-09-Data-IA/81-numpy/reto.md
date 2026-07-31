# Reto 81: El Cajero Automático Veloz

Eres el programador del cajero de un supermercado. Hoy es el "Día de Locura" y todos los productos tienen un descuento especial.

Tienes una lista con los precios base de 4 productos: 50, 120, 300, 45.

Tu misión es aplicarles un descuento de 20 dólares a **todos** los productos al mismo tiempo.

### Pasos a seguir:
1. Trae tu herramienta matemática `numpy` y ponle su apodo `np`.
2. Crea una variable llamada `precios_base`.
3. Usa `np.array()` para guardar la lista de los 4 precios `[50, 120, 300, 45]` dentro de esa variable.
4. Crea una segunda variable llamada `precios_descuento`.
5. Asigna a `precios_descuento` el resultado de restarle 20 a tus `precios_base`.
6. Imprime en pantalla la variable `precios_descuento`.

### Reglas estrictas:
- **PERMITIDO:** `import numpy as np`, `np.array()`, hacer restas (`-`), usar `print()`.
- **PROHIBIDO:** Usar `for`, usar `while`, restar los números mentalmente y escribirlos a mano. ¡Deja que Numpy trabaje!

### Resultado esperado en la terminal:
```text
[ 30 100 280  25]
```
