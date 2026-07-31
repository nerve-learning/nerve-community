# Reto 53: El Registro de Asistencia 📝

Estás organizando la fiesta más grande del año. Cada vez que llega un invitado, necesitas anotar su nombre en una lista oficial de asistencia en un archivo de texto. ¡Vamos a automatizar esto!

### Instrucciones paso a paso:

1. Crea una variable llamada `invitados` que contenga una lista (con corchetes `[]`) con los nombres de 3 amigos tuyos.
2. Crea una función (con `def`) llamada `registrar_invitados(lista)` que reciba esa lista de amigos como parámetro.
3. Dentro de la función, usa el guardián `with open(...)` para abrir un archivo llamado `"asistencia.txt"`. Ábrelo en el modo para escribir desde cero (modo `"w"`).
4. Dentro del bloque `with`, usa `.write()` para escribir el título `"--- LISTA DE INVITADOS ---\n"`. ¡No olvides el salto de línea `\n`!
5. Crea un bucle `for` para recorrer cada amigo dentro de tu lista recibida.
6. Adentro del bucle, por cada amigo, usa `.write()` para escribir su nombre en el archivo seguido de un salto de línea (`nombre + "\n"`).
7. Afuera de la función, llámala pasándole tu variable `invitados`.
8. Corre tu código. 
9. **(Opcional para curiosos)**: Abre tu código, cambia la letra `"w"` por `"a"`. Vuelve a correr el código. ¡Abre el archivo `asistencia.txt` en tu bloc de notas y observa cómo todos los invitados se duplicaron al final!

---

### 🟢 Conceptos Permitidos (Lo único que puedes usar)
* Asignación de variables (`=`)
* Listas y bucles (`for elemento in lista:`)
* Funciones (`def nombre_funcion(parametro):`)
* Escribir archivos (`with open(archivo, "w") as apodo:` o `"a"`)
* Escribir texto (`apodo.write()`)
* Salto de línea (`\n`)
* Sumar textos (`"Hola " + nombre`)

### 🔴 Prohibido
* Usar el modo lectura (`"r"`).
* Abrir el archivo usando `open()` sin usar el guardián `with`.
* Escribir los nombres uno por uno de forma manual (¡usa tu bucle `for`!).
* Olvidar el salto de línea `\n`.

---

### 🎯 Resultado esperado
*(No verás nada impreso en la terminal. El resultado estará dentro del archivo "asistencia.txt" que tu código creará automáticamente. Debería verse así si lo abres con tu bloc de notas:)*

```text
--- LISTA DE INVITADOS ---
Ana
Beto
Carlos
```

¡Demuestra que puedes controlar los registros de la fiesta!
