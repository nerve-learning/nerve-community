# Teoría: Las Dos Caras de la Moneda

En Python, todo lo que creas cae en una de dos categorías: **Mutable** o **Inmutable**.

## 1. Los Inmutables (Sellados)
Números, Textos y Tuplas.
Una vez creados, su valor *interno* no puede cambiar. Si tienes una variable con el número `5` y luego le sumas `1`, Python destruye el `5` y crea una nueva caja con el `6`.
- **Intento fallido de cambiar un texto:** No puedes cambiar la primera letra de un texto usando posiciones (como `texto[0] = "H"`). ¡Están sellados!

## 2. Los Mutables (Cambiables)
Listas, Diccionarios y Sets.
Puedes abrirlos, sacar cosas y meter cosas nuevas. La caja sigue siendo la misma, solo cambia lo de adentro.

## La Trampa del Igual `=` (El efecto Espejo)
Aquí está el peligro. Cuando haces esto con números (inmutables), todo funciona como esperas:
```python
a = 10
b = a
a = 20
# 'b' sigue valiendo 10. ¡Eran cajas separadas!
```

¡Pero mira lo que pasa con las Listas (mutables)!
```python
lista_A = [1, 2, 3]
lista_B = lista_A
lista_A.append(4)
```
Si imprimes `lista_B`, ¡también tendrá el `4`! 
¿Por qué? Porque el símbolo `=` en los Mutables **no hace una copia**. Simplemente le pone una "segunda etiqueta" a la misma caja física. `lista_A` y `lista_B` son como dos controles remotos apuntando a la misma televisión. Si uno cambia de canal, el otro también lo ve.

## ¿Qué pasa si me equivoco?

**El error más común:** Modificar una lista pensando que es una copia segura.
Si le pasas tu lista de usuarios a una parte del programa para que la "revise", y esa parte decide borrar un usuario... ¡Lo borrará de tu lista original también! Para evitarlo, tienes que aprender a hacer "clones reales".
