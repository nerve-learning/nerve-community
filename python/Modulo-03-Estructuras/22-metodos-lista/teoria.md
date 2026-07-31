# Teoría: Órdenes directas a la Lista

Para modificar una lista que ya existe, usamos un nuevo símbolo: **el punto `.`**

El punto se coloca justo después del nombre de la variable y significa: "A esta variable, hazle lo siguiente". A las acciones que van después del punto las llamamos **Métodos**.

## 1. Agregar al final: `.append()`
La palabra "append" significa "adjuntar" o "añadir al final". 

### Anatomía de append
```python
mochila = ["Mapa"]
mochila.append("Poción")
```
Desmontemos `mochila.append("Poción")`:
- `mochila`: Es a quién le estamos dando la orden (nuestra lista).
- `.`: El "comunicador". Conecta la lista con la orden.
- `append`: La orden en sí ("añade al final").
- `()`: Los paréntesis son como una caja de envío. Aquí ponemos lo que necesita la orden para funcionar.
- `"Poción"`: Lo que estamos enviando para que se guarde en la lista.

## 2. Quitar por nombre: `.remove()`
La palabra "remove" significa "remover" o "quitar". Busca exactamente lo que le pidas y saca el **primero** que encuentre.

### Anatomía de remove
```python
mochila.remove("Mapa")
```
Funciona igual: "A la mochila (`mochila`), aplícale la orden de quitar (`.remove`), y aquí te envío lo que quiero que quites (`("Mapa")`)".

## ¿Qué pasa si me equivoco?

**Error común 1: Olvidar los paréntesis `()`**
Si escribes:
```python
mochila.append
```
La computadora dirá "Ok, veo que quieres usar append, pero no lo estás ejecutando". ¡Los paréntesis son los que obligan a la orden a ejecutarse!

**Error común 2: Intentar quitar algo que no existe**
Si escribes:
```python
mochila.remove("Dragón")
```
Pero `"Dragón"` no está en tu mochila, la terminal entrará en pánico y mostrará un error: `ValueError: list.remove(x): x not in list` (El valor no está en la lista). ¡Solo puedes sacar lo que ya está adentro!
