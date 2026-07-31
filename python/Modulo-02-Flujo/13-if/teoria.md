# Teoría: El guardavías de Python (`if`)

Para hacer que Python tome una decisión, usamos la palabra reservada `if` (que en inglés significa "si...", de condición, no de afirmación).

Piensa en `if` como un guardia frente a una puerta. El guardia te hace una pregunta que se responde con `True` o `False`.
* Si la respuesta es `True`, la puerta se abre y entras a hacer lo que hay adentro.
* Si la respuesta es `False`, la puerta se queda cerrada y te saltas ese cuarto por completo.

### Los dos puntos (`:`)
En español, cuando contamos una historia solemos decir: "Si llueve, entonces...". 
En Python, los dos puntos `:` significan exactamente ese "entonces". Le dicen a la computadora que la condición terminó y viene la consecuencia.

### La regla de oro: La Indentación (Sangría)
En Python, ¿cómo sabe la computadora qué código pertenece adentro de la puerta del `if` y qué código va después? 
¡Con espacios! Todo lo que esté "dentro" del `if` **debe estar empujado hacia la derecha**. 
A esto se le llama **indentación**. Normalmente usamos la tecla `Tab` o 4 espacios. En cuanto dejas de empujar el código a la derecha, Python sabe que ya saliste del `if`.

---

## Anatomía (Sintaxis)

```python
if condicion:
    print("Esto solo pasa si la condición es True")
    print("Esto también")
print("Esto pasa siempre, porque ya no tiene sangría")
```

* `if`: La palabra mágica, siempre en minúsculas.
* `condicion`: Lo que evaluamos (ej. `edad >= 18`). Debe dar como resultado `True` o `False`.
* `:` : Los dos puntos. Obligatorios. Significan "entonces...".
* `    `: La sangría (4 espacios). Le dice a Python que esa línea es la consecuencia del `if`.

---

## ¿Qué pasa si me equivoco?

**1. El infame "IndentationError"**
Si olvidas poner la sangría, o pones 3 espacios en una línea y 4 en otra, Python se detendrá en seco y te lanzará un `IndentationError`. 
* ¿Por qué? Python es un obsesivo del orden. Si no alineas bien el código, no sabe a quién le pertenece.
* **Solución:** Borra los espacios y presiona la tecla `Tab` una vez. Sé consistente.

**2. Olvidar los dos puntos (`SyntaxError: invalid syntax`)**
Si escribes `if edad >= 18` y le das Enter sin poner los `:`, Python llorará porque no sabe dónde termina la pregunta.
* **Solución:** Pon siempre `:` al final del renglón del `if`.
