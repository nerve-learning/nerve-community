# Teoría: Bucles Anidados

Imagina que eres un cartero entregando cartas en un edificio. Tu rutina es:
1. Entrar al Piso 1.
2. Caminar por la puerta A, luego la B, luego la C.
3. Subir al Piso 2.
4. Caminar por la puerta A, luego la B...

En programación, el Piso es nuestra lista exterior, y las puertas son las listas interiores. Para hacer esta rutina, necesitamos **bucles anidados** (un bucle dentro de otro).

## Anatomía de una Matriz y Bucles Anidados

```python
# Nota cómo hay corchetes dentro de otros corchetes
edificio = [
    ["Puerta 1A", "Puerta 1B"],
    ["Puerta 2A", "Puerta 2B"]
]

for piso in edificio:
    print("¡Llegué a un nuevo piso!")
    
    # Este bucle está ADENTRO del primer bucle
    for puerta in piso:
        print("Revisando la:", puerta)
```

Desmontemos la estructura:

- `[ [ ... ], [ ... ] ]` : Estos son los corchetes dobles. La lista principal (`edificio`) contiene otras dos listas adentro (los pisos). A esto le llamamos **Matriz** o arreglo de 2 dimensiones (2D).
- `for piso in edificio:` : Nuestro bucle principal. En cada vuelta, agarrará **una lista completa** (un piso) y la guardará en la variable temporal `piso`.
- `for puerta in piso:` : ¡El bucle interior! Como `piso` es una lista, podemos recorrerla. Nota el **doble nivel de indentación**. Este bucle sacará cada elemento (texto) de la lista `piso`.

La regla de oro: **Por cada vuelta del bucle de afuera, el bucle de adentro tiene que dar todas sus vueltas completas.**

## ¿Qué pasa si me equivoco?

El error más común es confundir los niveles de indentación (los espacios a la izquierda).

**¿Qué pasa si olvido indentar el segundo bucle?**
Si el segundo `for` no está empujado hacia la derecha, la computadora pensará que es un bucle independiente. Intentará recorrer `piso`, pero como está fuera del primer bucle, es muy probable que cause un error o que solo recorra el último piso del edificio.

**¿Qué pasa si imprimo `piso` directamente?**
Si haces `print(piso)` sin usar el segundo bucle, verás en tu pantalla algo como `['Puerta 1A', 'Puerta 1B']`. Estarás viendo la caja entera en lugar de su contenido individual.
