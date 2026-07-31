# Teoría: La Voz del Objeto 🗣️

Imagina que le preguntas a un extraño en la calle: *"¿Quién eres?"*. 
Si no tiene una voz para hablarte, simplemente te mostrará su número de documento de identidad (algo como `0x7f8b9c2a10`). Así nacen los objetos en Python: mudos.

El método mágico `__str__` (abreviatura de *string* o cadena de texto) es la forma en la que le damos una voz a nuestro objeto. 

Cuando tú escribes `print(mi_objeto)` en tu código, Python detrás de escena va y le pregunta al objeto: *"Oye, ¿tienes el método mágico `__str__`? Si lo tienes, dime qué texto quieres que yo muestre en la pantalla"*.

---

## 🧬 Anatomía del `__str__`

```python
class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __str__(self):
        # Esta es la voz del gato. ¡Siempre debe usar return!
        return f"Un hermoso gato llamado {self.nombre}"
```

1. **Los dobles guiones bajos (`__str__`):** Le avisan a Python que no es una función normal, sino un hechizo que debe ejecutarse automáticamente cuando alguien use `print()` sobre el objeto.
2. **El `return` obligatorio:** Esta función **nunca** debe imprimir cosas directamente. Su único trabajo es *devolverle* un texto a Python para que Python sea quien lo imprima.

---

## 🚨 ¿Qué pasa si me equivoco?

El error más trágico y común de este nivel tiene que ver con olvidar cómo funciona el `return`.

**Usar `print()` dentro de `__str__`:**
```python
def __str__(self):
    print(f"Soy {self.nombre}") # ❌ ¡MAL!
```
Si haces esto, la terminal te gritará con este error:
> `TypeError: __str__ returned non-string (type NoneType)`

*Razón:* Python te está diciendo: *"Oye, te pedí que me devolvieras (return) un texto para yo poder imprimirlo, pero no me devolviste nada (NoneType) porque usaste print en su lugar"*.

*Solución:* **Siempre** usa `return` dentro de `__str__`. Deja que el `print()` lo haga quien esté afuera usando el objeto.
