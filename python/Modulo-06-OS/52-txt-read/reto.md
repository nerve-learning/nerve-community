# Reto 52: El Lector de Diarios 📖

Tu amigo te dejó su diario guardado en un archivo de texto, pero le da pereza contar cuántas letras ha escrito. Como eres un programador en entrenamiento, vas a automatizar esa tarea.

### Instrucciones paso a paso:

1. Crea un archivo llamado `diario.txt` en la misma carpeta que tu código. Escribe adentro 3 líneas de texto contándome cómo estuvo tu día. ¡Guárdalo!
2. Ahora, en tu archivo de Python, crea una función (con `def`) llamada `leer_diario(nombre_archivo)` que reciba el nombre de un archivo como parámetro.
3. Dentro de la función, usa el bloque mágico `with open(...)` para abrir el archivo que recibiste como parámetro. Recuerda usar el modo lectura (`"r"`).
4. Adentro del bloque `with`, lee el contenido completo usando `.read()` y guárdalo en una variable llamada `texto`.
5. Imprime el mensaje: `"Mi diario dice:"` seguido del contenido de la variable `texto`.
6. **(Bono de niveles pasados)**: Usa la función `len()` con tu variable `texto` para saber cuántas letras (caracteres) tiene, y guárdalo en una variable llamada `cantidad`.
7. Imprime el mensaje: `"El diario tiene [cantidad] caracteres en total."`
8. Afuera de la función, llámala pasándole el texto exacto `"diario.txt"`.

---

### 🟢 Conceptos Permitidos (Lo único que puedes usar)
* Asignación de variables (`=`)
* Funciones (`def nombre(parametro):`)
* Abrir archivos (`with open(archivo, "r") as apodo:`)
* Leer texto (`apodo.read()`)
* Contar elementos (`len()`)
* Imprimir texto (`print()`)

### 🔴 Prohibido
* Copiar y pegar código de internet.
* Usar `import os` (no lo necesitamos hoy, el archivo está aquí mismo).
* Usar herramientas avanzadas como `.readlines()` o bucles `for` para recorrer el archivo línea por línea (hoy leemos todo de un solo golpe con `.read()`).

---

### 🎯 Resultado esperado en la terminal
*(Nota: El texto exacto de tu diario y la cantidad de caracteres dependerán de lo que hayas escrito en `diario.txt`, pero el formato debe ser igual a este)*

```text
Mi diario dice: 
Hoy aprendí a leer archivos en Python.
Fue un buen día.
Espero no olvidar el 'with'.

El diario tiene 87 caracteres en total.
```

¡Demuestra que puedes leer cualquier secreto! Recuerda el error de la caja fantasma si Python te grita.
