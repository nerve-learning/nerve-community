# Teoría: El Nacimiento de tus Propios Comandos 🛠️

Piensa en una **función** como si fuera la receta de un pastel guardada en un libro. 
Mientras la receta está en el libro, no hace nada; es solo texto. Para tener un pastel, alguien tiene que ir, leer la receta, y ejecutar los pasos.

En Python ocurre exactamente lo mismo:
1. **Definir la función:** Es escribir la receta en el libro.
2. **Llamar a la función:** Es darle la orden a Python de que vaya al libro y cocine la receta en ese preciso momento.

## 🧬 Anatomía de una Función (Paso a paso)

Para inventar un nuevo comando, usamos esta estructura:

```python
def mostrar_bienvenida():
    print("¡Hola!")
    print("Bienvenido a nuestro sistema.")
```

Vamos a desarmar los símbolos (nuestro desmontaje conceptual):

- `def`: Es una palabra reservada (propia de Python) que significa **"define"** (o "voy a inventar algo nuevo"). Le avisa a la computadora: "Atención, lo que viene no es para ejecutarlo ya, es para guardarlo".
- `mostrar_bienvenida`: Es el **nombre** que tú eliges para tu función. Debe usar letras minúsculas y guiones bajos (snake_case). Este será el nombre de tu comando.
- `()`: Son los paréntesis. Por ahora están vacíos. Imagina que son una "bandejita" donde más adelante pondremos ingredientes. Aunque no necesites ingredientes hoy, la bandejita **tiene que estar**. Es la regla de oro para que Python sepa que es una función y no una variable.
- `:`: Los dos puntos significan **"aquí empiezan los pasos a guardar"**.
- **Indentación (los 4 espacios a la izquierda):** Igual que en los `if` o `for`, todo lo que esté "metido hacia la derecha" es lo que pertenece a esta función. En cuanto el código vuelva al margen izquierdo, la función habrá terminado.

### ¿Cómo ordeno que se ejecute? (Llamar a la función)

Una vez que la has definido, en cualquier parte de tu código más abajo, solo escribes su nombre seguido de los paréntesis:

```python
mostrar_bienvenida()
```
¡Boom! Python busca la receta llamada `mostrar_bienvenida`, ejecuta los dos `print`, y luego sigue con el resto de tu código.

---

## 🚨 ¿Qué pasa si me equivoco?

### Error 1: Olvidar los dos puntos `:` o los paréntesis `()`
**El síntoma en la terminal:** `SyntaxError: expected ':'` o `SyntaxError: invalid syntax`
**¿Por qué pasa?** Porque rompiste la gramática de Python. La computadora lee `def mi_comando` y se queda esperando los símbolos que completan la declaración. ¡Revisa el final de la línea!

### Error 2: Escribir el código y que no pase absolutamente nada en pantalla
**El síntoma en la terminal:** El programa termina y no hay texto, no hay errores, simplemente nada.
**¿Por qué pasa?** ¡Escribiste la receta en el libro pero **nunca le diste la orden de cocinarla**! 
Definir la función (`def`) solo la guarda en memoria. Tienes que "llamarla" escribiendo su nombre con paréntesis en el margen izquierdo: `mi_comando()`.

### Error 3: IndentationError
**El síntoma en la terminal:** `IndentationError: expected an indented block`
**¿Por qué pasa?** Pusiste los dos puntos `:`, pero en la línea de abajo empezaste a escribir pegado al borde izquierdo. Python exige que los pasos de la función tengan espacios a la izquierda para saber qué pertenece adentro y qué queda afuera.
