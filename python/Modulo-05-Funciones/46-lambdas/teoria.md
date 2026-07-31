# Teoría: El Post-it de Python 🟨

Una función Lambda hace exactamente lo mismo que un `def`, pero con reglas muy estrictas:
- **Solo puede tener una línea de código.**
- **No se usa la palabra `return`.** (Python asume automáticamente que el resultado de esa única línea es lo que quieres devolver).
- **No tiene nombre por defecto.** (Aunque puedes guardarla en una variable).

## 🧬 Anatomía de una Lambda

Mira cómo convertimos esto:
```python
def sumar(a, b):
    return a + b
```

En esto (la versión Lambda):
```python
sumar = lambda a, b : a + b
```

Vamos a desarmar el "Post-it":
- `lambda`: Es la palabra mágica. Significa *"Voy a crear una función rápida de una línea"*.
- `a, b`: Son los parámetros (nuestra bandejita de ingredientes). Fíjate que **NO usan paréntesis**.
- `:`: Los dos puntos separan los ingredientes del cálculo matemático.
- `a + b`: Es la operación. Python calcula esto y **automáticamente hace el `return`** por ti. ¡No lo escribas!

## ¿Por qué dice "anónima"?
Porque las lambdas nacieron para usarse sin nombre, pasándolas directamente a otros sistemas (lo veremos más adelante en tu carrera). Sin embargo, hoy las guardaremos en variables (como `sumar = lambda...`) para que aprendas su estructura y puedas usarlas fácilmente.

---

## 🚨 ¿Qué pasa si me equivoco?

### Error 1: Intentar poner múltiples líneas
**El síntoma en la terminal:** `SyntaxError: invalid syntax`
**¿Por qué pasa?** Las Lambdas son Post-its pequeñitos. No puedes meter bucles `for`, ni `while`, ni crear múltiples variables dentro de una lambda. **Debe ser una sola expresión matemática o de texto directa.** Si necesitas más de una línea, ¡usa un `def` formal!

### Error 2: Escribir la palabra 'return'
**El síntoma en la terminal:** `SyntaxError: invalid syntax`
**¿Por qué pasa?** Escribir `lambda x: return x * 2` es un error. La magia de las lambdas es que el `return` es invisible y automático. Python ya sabe que tiene que devolver el resultado de la derecha.

### Error 3: Poner paréntesis en los parámetros
**El síntoma en la terminal:** (Depende del contexto, a veces funciona como tupla, pero es una mala práctica visual).
**¿Por qué pasa?** Por costumbre del `def`. En `lambda (x, y):` los paréntesis no son necesarios para los parámetros. Escribe simplemente `lambda x, y :`.
