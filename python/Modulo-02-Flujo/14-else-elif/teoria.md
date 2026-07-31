# Teoría: El Plan B y las múltiples rutas

Cuando usamos un `if` solitario, solo tenemos un "Plan A". Si la condición del `if` es mentira (`False`), la computadora se salta todo y sigue su camino en silencio. 
Pero casi siempre queremos hacer *otra* cosa si la condición falla.

### El Plan B: `else` (Y si no...)
La palabra `else` significa "de lo contrario". Actúa como una red de seguridad. Le dice a Python: "Si el `if` de arriba falló y no abriste su puerta, entra por esta puerta automáticamente, sin hacer preguntas".
* **Regla estricta:** Un `else` NUNCA lleva una condición al lado (no hace preguntas, solo actúa). Siempre va seguido de dos puntos `:`.

### Los Planes C, D, E...: `elif` (Pero si en cambio...)
¿Qué pasa si hay 3, 4 o 5 opciones? Por ejemplo, las luces de un semáforo. No es solo "Rojo o no Rojo".
Para eso existe `elif` (una abreviatura de "else if", que significa "pero si en cambio..."). 
Te permite hacer una nueva pregunta si el `if` anterior falló. Puedes poner todos los `elif` que quieras uno debajo de otro.

---

## Anatomía (Sintaxis)

```python
if condicion_1:
    print("Plan A")
elif condicion_2:
    print("Plan B")
elif condicion_3:
    print("Plan C")
else:
    print("Plan Z (Si TODO lo anterior falló)")
```

* El orden **SIEMPRE** debe ser: un `if` primero, luego los `elif` (opcionales), y al final un único `else` (opcional).
* Observa que `if` y `elif` llevan una condición antes de los `:`.
* El `else` **nunca** lleva condición. Solo lleva `:`.
* Todos (`if`, `elif`, `else`) van pegados a la pared izquierda (sin sangría), pero lo que hay *adentro* de ellos sí debe tener sangría (4 espacios).

---

## ¿Qué pasa si me equivoco?

**1. SyntaxError: `else` con condición**
Si escribes `else edad < 18:`, Python no entenderá. El `else` es el basurero final, el "si nada funcionó, haz esto". No necesita condiciones.
* **Solución:** Bórrale la condición y déjalo solo como `else:`. Si necesitas hacer otra pregunta, usa `elif`.

**2. IndentationError en el `else`**
Si empujas el `else` hacia la derecha (con espacios) para que quede debajo de los `print`, Python dirá que ese `else` está huérfano. 
* **Solución:** Los `if`, `elif` y `else` deben estar perfectamente alineados entre sí a la izquierda.
