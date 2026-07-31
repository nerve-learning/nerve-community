# Teoría: El Botón de Parada

Hasta ahora, nuestros bucles `for` y `while` eran imparables. Una vez que empezaban, tenían que terminar de revisar toda la lista o esperar a que la condición principal se volviera falsa. 

La palabra reservada `break` (que significa "romper" o "detener" en inglés) nos permite destruir el bucle desde adentro y salir de él inmediatamente.

## Anatomía de un `break`

Casi siempre, el `break` va a vivir escondido dentro de un `if`. ¡Tiene sentido! Solo queremos jalar el freno de emergencia **SI** pasa algo específico.

```python
cajon = ["lápiz", "goma", "llave", "moneda"]

for objeto in cajon:
    print("Revisando:", objeto)
    
    if objeto == "llave":
        print("¡La encontré!")
        break
```

Desmontemos la nueva herramienta:

- `break` : Es una orden directa a la computadora que dice "destruye el bucle en el que estamos atrapados y salta al código que está abajo del todo". No requiere paréntesis, ni signos especiales. Solo la palabra.
- La indentación : Nota cómo el `break` está doblemente indentado. Primero, está dentro del `for`. Segundo, está dentro del `if`. 

## ¿Qué pasa si me equivoco?

El error más común es usar el freno de emergencia donde no hay ningún vehículo en movimiento.

**¿Cómo se ve el error?**
`SyntaxError: 'break' outside loop`

**¿Por qué pasa?**
Pasa cuando escribes la palabra `break` pero no estás dentro de un bloque `for` ni de un bloque `while`. La computadora dice: "¿Qué quieres que detenga si no estamos repitiendo nada?".

**¿Cómo lo soluciono?**
Asegúrate de que la palabra `break` tenga al menos un nivel de indentación (espacios a la izquierda) y que arriba de ella, en algún lugar, exista un `for` o un `while` que la contenga. Y recuerda: `break` solo rompe **un** bucle, el que lo encierra directamente.
