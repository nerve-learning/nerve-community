# Reto 11: La Montaña Rusa "El Dragón" 🐉

El parque de diversiones local te contrató para automatizar el acceso a su montaña rusa más extrema. Tienen reglas de seguridad muy estrictas sobre quién puede subir y quién recibe descuentos. Tu trabajo es programar las variables que deciden si el visitante entra o no.

## Instrucciones

1. Crea variables iniciales para un visitante imaginario (asígnales valores tú mismo):
   * Su altura en centímetros (un número entero, ej. `150`).
   * Su edad (un número entero, ej. `13`).
   * Si es un residente local (un valor booleano: `True` o `False`).

2. **Regla de acceso (usa `and`)**: 
   Por seguridad, para subir a la montaña rusa la persona debe medir más de 140 centímetros **Y** tener 12 años o más.
   Crea una variable llamada `puede_subir` que evalúe las variables anteriores y guarde el resultado (`True` o `False`).

3. **Regla de descuento (usa `or`)**: 
   La persona recibe descuento en la tienda de recuerdos si es menor de 15 años **O** si es residente local (`True`).
   Crea una variable llamada `tiene_descuento` que evalúe las variables anteriores y guarde el resultado.

4. Muestra en pantalla los resultados finales utilizando `f-strings`.

### Conceptos permitidos
- Variables (asignación con `=`).
- Tipos de datos básicos (`int`, `bool`).
- Operadores de comparación (`>`, `<`, `>=`).
- Operadores lógicos (`and`, `or`, `not`).
- Imprimir en pantalla con `print()` y variables inyectadas con `f-strings`.

### Conceptos prohibidos
- Condicionales (`if`, `else`, `elif`). No dejes que la computadora tome la ruta aún, solo muéstranos el `True` o `False` en bruto.
- Funciones `def`.
- Listas `[]` o diccionarios `{}`.

### Resultado esperado en terminal
Si configuras a tu visitante ficticio con: `altura = 150`, `edad = 13` y `residente = False`, al correr tu código la terminal debe verse exactamente así:

```text
--- Control de Acceso: El Dragón ---
¿El visitante puede subir a la montaña rusa?: True
¿El visitante tiene derecho a descuento?: True
```
