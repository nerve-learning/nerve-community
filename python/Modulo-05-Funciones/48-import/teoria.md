# Teoría: La Ferretería de Python 🛠️

Por defecto, Python es ligero. Solo te da un cinturón básico con herramientas pequeñas (como `print()` o `len()`). Si quieres más, tienes que ir a buscar la caja de herramientas específica.

## 1. Traer la caja entera (`import`)

La palabra mágica `import` significa *"Trae esta caja de herramientas y déjala en el suelo"*.

```python
import math
```
Cuando traes la caja entera, para usar una herramienta **tienes que decir en qué caja está**. Lo haces poniendo el nombre de la caja, un punto `.`, y luego la herramienta:

```python
raiz = math.sqrt(9) # La caja 'math' tiene una herramienta 'sqrt' (raíz cuadrada)
```

## 2. Sacar solo una herramienta de la caja (`from ... import ...`)

Si la caja de herramientas pesa mucho y tú solo necesitas el martillo, puedes usar la estructura `from` (desde) e `import` (importar).

```python
from random import randint
```
Significa: *"Desde la caja `random`, sácame solo la herramienta `randint`"*.
Como ya la tienes en la mano (y no en el suelo), **ya no usas el punto ni el nombre de la caja**:

```python
dado = randint(1, 6) # La usas directamente
```

---

## 🚨 ¿Qué pasa si me equivoco?

### Error 1: Escribir mal el nombre de la caja
**El síntoma en la terminal:** `ModuleNotFoundError: No module named 'matematicas'`
**¿Por qué pasa?** Le pediste a Python una caja que no existe. ¡Las cajas oficiales tienen nombres estrictos en inglés! Es `math`, no `matematicas` o `Math` (con mayúscula).

### Error 2: Olvidar decir de qué caja viene la herramienta
**El síntoma en la terminal:** `NameError: name 'sqrt' is not defined`
**¿Por qué pasa?** Usaste `import math` (trajiste la caja al suelo), pero luego escribiste `resultado = sqrt(9)` sin el `math.`. Python no sabe de dónde salió ese `sqrt`. ¡Recuerda el punto!

### Error 3: Escribir el import en medio del código
*(No es un error que explote, pero es una pésima práctica)*. 
**Regla de oro:** Todos los `import` van en la **línea 1** de tu archivo, hasta arriba de todo. Piensa que antes de empezar a trabajar en la obra, tienes que bajar todas las cajas de herramientas de tu camión. No vas a buscar la caja a mitad de la construcción.
