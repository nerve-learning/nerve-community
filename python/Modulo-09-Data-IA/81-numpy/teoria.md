# Teoría: El poder de hacer las cosas "de golpe"

Hasta ahora, si queríamos modificar varios números, usábamos un bucle `for` para ir uno por uno. Numpy cambia las reglas del juego. 

Para usar Numpy, primero tenemos que traerlo a nuestro programa y, por convención mundial, le ponemos un apodo corto: `np`.

## Anatomía de Numpy

```python
import numpy as np
```
- **`import numpy`**: Le dice a la computadora "trae la caja de herramientas matemática".
- **`as np`**: Le dice "para no escribir 'numpy' cada vez, te llamaré 'np'". Es como un apodo.

```python
mi_super_lista = np.array([1, 2, 3])
```
- **`np.`**: Usa la herramienta 'np'.
- **`array`**: Es el creador de súper listas (su nombre técnico es arreglo o vector).
- **`(...)`**: Los paréntesis para ejecutar la acción de crear.
- **`[...]`**: Los corchetes de la lista normal que le estamos entregando para que la transforme.

```python
resultado = mi_super_lista + 10
```
- **`+ 10`**: Al sumarle 10, Numpy es tan inteligente que sabe que no quieres sumar 10 al final de la lista, sino sumarle 10 a **cada uno de los números por separado**. 

## ¿Qué pasa si me equivoco?

### Error 1: Olvidar los corchetes
**El error:** `np.array(1, 2, 3)`
Si haces esto, la terminal gritará un error raro como:
`TypeError: array() takes from 1 to 2 positional arguments but 3 were given`
**¿Por qué?** Porque `array` espera recibir **una sola caja** (una lista con corchetes `[]`), no tres números sueltos.
**La solución:** Envuelve tus números en corchetes antes de dárselos a Numpy: `np.array([1, 2, 3])`.

### Error 2: Intentar sumar una lista normal
**El error:** `[1, 2, 3] + 5`
La terminal te dirá:
`TypeError: can only concatenate list (not "int") to list`
**¿Por qué?** Python normal no sabe cómo sumar un número suelto a una lista de cosas. Piensa que intentas "pegar" un número al final de la lista, pero para pegar cosas en listas normales, ambas deben ser listas. Numpy sí entiende que quieres hacer matemáticas.
