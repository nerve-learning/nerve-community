# Teoría: El Revisor de Listas

Imagina que tienes una lista de tareas. Para completarlas, tomas la primera, la haces; luego la segunda, la haces; y así hasta terminar. 

El bucle `for` está diseñado exactamente para eso: **recorrer estructuras que tienen varios elementos**, como las listas que aprendiste a crear con los corchetes `[]`.

## Anatomía de un `for`

```python
mochila = ["espada", "escudo", "poción"]

for objeto in mochila:
    print("He sacado un:")
    print(objeto)
```

Desmontemos cada palabra y símbolo:

- `for` : Significa "por cada". Le dice a la computadora que vamos a revisar una colección de cosas.
- `objeto` : Esta es una **variable temporal** o "etiqueta mágica". La computadora tomará el primer elemento de la lista (`"espada"`) y lo guardará aquí. Cuando el bloque de código termine, tomará el segundo elemento (`"escudo"`) y lo guardará aquí, reemplazando al anterior. ¡Tú inventas este nombre! Podría llamarse `item`, `cosa` o `x`.
- `in` : Significa "en". Conecta nuestra variable temporal con la lista que queremos revisar.
- `mochila` : Es la lista (o colección) que estamos recorriendo.
- `:` : Los dos puntos. Al igual que en `if` y `while`, significa "entonces haz lo siguiente".
- La indentación (espacios al inicio) : Todo lo que esté empujado a la derecha es lo que se hará **con cada elemento** de la lista.

La computadora lee esto como: "Por cada `objeto` en la `mochila`, haz lo siguiente".

## ¿Qué pasa si me equivoco?

El error más común es intentar usar `for` en algo que no se puede "recorrer" o "dividir en partes".

**¿Cómo se ve el error?**
`TypeError: 'int' object is not iterable`

**¿Por qué pasa?**
Imagina que le dices a la computadora: "Por cada elemento en el número 5". La computadora te mirará confundida. El número 5 es solo una cosa sólida, no es una lista ni una caja con cosas adentro. En programación, a las cosas que se pueden recorrer (como las listas) se les llama "iterables".

**¿Cómo lo soluciono?**
Asegúrate de que la variable que está después de la palabra `in` sea una lista (que tenga corchetes `[]`). Nunca intentes hacer un `for` directamente sobre un número.
