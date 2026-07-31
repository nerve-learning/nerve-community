# Abriendo y Leyendo Archivos

Imagina que un archivo de texto es como un sobre cerrado que contiene una carta. Para leer la carta, Python tiene que hacer un ritual de 3 pasos:

1. **Abrir el sobre** con cuidado.
2. **Sacar la carta** y leer el texto.
3. **Cerrar el sobre** y guardarlo para que la carta no se pierda ni se arruine con el viento.

Afortunadamente, Python nos da una herramienta mágica llamada `with` que se encarga de abrir y cerrar el sobre automáticamente, para que nosotros solo nos preocupemos de leer.

---

### Anatomía de los nuevos símbolos

Este es el bloque de código estándar para leer un archivo:

```python
with open("mensaje.txt", "r") as archivo:
    contenido = archivo.read()
```

* **`with`**: Es la palabra mágica (el guardián). Significa: *"Mientras mantengas abierta esta puerta, haz lo que dice abajo. Cuando termines (cuando se acabe la indentación), CÍERRALA por mí."* Nos protege de olvidar cerrar el archivo.
* **`open`**: Es la herramienta que abre la caja o archivo.
* **`"mensaje.txt"`**: El primer ingrediente (parámetro) de `open`. Es el nombre exacto del archivo que queremos abrir. Tiene que estar entre comillas porque es texto.
* **`"r"`**: El segundo ingrediente. Significa **"Read"** (Leer en inglés). Le estamos diciendo a Python: *"Solo quiero mirar, prometo no borrar ni escribir nada nuevo"*.
* **`as archivo`**: Significa **"y llámalo así"**. Le estamos poniendo el apodo `archivo` a nuestro sobre abierto para poder referirnos a él en las siguientes líneas.
* **`:`**: (Dos puntos). Al igual que en los `if` o bucles `for`, significa *"lo que viene a continuación con sangría (indentación) es lo que voy a hacer mientras esté abierto"*.
* **`archivo.read()`**: Tomamos nuestro sobre abierto (`archivo`), usamos el punto (`.`) para decirle qué hacer, y usamos la herramienta `read()` para sacar TODO el texto que tenga adentro.
* **`=`**: (Asignación). Guardamos todo ese gran bloque de texto que leímos en nuestra variable `contenido`.

---

### ⚠️ ¿Qué pasa si me equivoco?

**El error de la caja fantasma**
Si le pides a Python que abra un archivo que no existe en esa habitación (carpeta), o si escribiste mal el nombre, verás este error en la terminal:

```text
FileNotFoundError: [Errno 2] No such file or directory: 'mensaje.txt'
```

**¿Qué significa esto en lenguaje humano?**
Python te está diciendo: *"Fui a buscar el sobre llamado 'mensaje.txt' que me pediste, miré por toda la habitación, ¡pero no existe! ¿Estás seguro de que lo creaste o de que lo escribiste bien?"*

**¿Cómo lo soluciono?**
Revisa que el archivo de texto exista exactamente en la misma carpeta donde está guardado tu código de Python. Revisa también que no le falte la extensión `.txt` en tu código (ej. `"mensaje"` vs `"mensaje.txt"`).
