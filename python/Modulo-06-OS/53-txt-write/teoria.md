# Escribir y Agregar Texto

Imagina que un archivo de texto es un cuaderno de notas.
Cuando leímos en el nivel anterior, usamos la letra `"r"` (Read) que nos permitía mirar el cuaderno pero sin tocar un lápiz.

Para escribir, tenemos dos letras nuevas, y actúan de formas muy distintas:
1. **Modo `"w"` (Write/Escribir)**: Es como arrancar TODAS las páginas de tu cuaderno, tirarlas a la basura, y empezar a escribir en la primera página totalmente en blanco. **¡Destruye lo que había antes!** Si el cuaderno no existía, Python va a la papelería y te compra uno nuevo (crea el archivo).
2. **Modo `"a"` (Append/Agregar)**: Es como buscar la última página escrita de tu cuaderno y continuar escribiendo justo debajo, sin borrar absolutamente nada del pasado.

---

### Anatomía de los nuevos símbolos

Esta es la sintaxis para crear y escribir un archivo:

```python
with open("mi_diario.txt", "w") as archivo:
    archivo.write("¡Hola, mundo!\n")
```

* **`"w"`**: Le dice a nuestro guardián (`with`) cómo quieres abrir el archivo. Si pones `"w"`, estás listo para destruir el pasado y escribir algo nuevo. Si pones `"a"`, estás listo para agregar al final.
* **`.write()`**: Es la herramienta (acción) para escribir texto dentro del archivo. A diferencia de `print()`, `.write()` **NO** salta a la siguiente línea automáticamente. Escribe todo seguido como un tren.
* **`\n` (Salto de línea)**: Es un símbolo invisible para los humanos pero muy claro para Python. La barra invertida `\` y la `n` (de *newline*) le dicen a la computadora: *"Aquí presiona la tecla Enter del teclado"*. Sin esto, todas tus frases quedarían pegadas en un solo renglón larguísimo.

---

### ⚠️ ¿Qué pasa si me equivoco?

**El error del tipo equivocado**
Imagina que quieres guardar tu puntuación (un número puro, como `100`), y haces esto: `archivo.write(100)`. Python te dará este error:

```text
TypeError: write() argument must be str, not int
```

**¿Qué significa esto en lenguaje humano?**
Python te dice: *"La herramienta `.write()` solo usa tinta (texto, que llamamos `str`). ¡Me estás pidiendo que meta un concepto matemático puro (un `int`) en un cuaderno de texto!"*

**¿Cómo lo soluciono?**
Simplemente disfraza tu número de texto convirtiéndolo con la función `str()`. Así:
`archivo.write( str(100) )` o combinándolo con un texto `archivo.write("Puntos: " + str(100))`
