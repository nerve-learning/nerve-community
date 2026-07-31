# Reto 31: El Contador de Cohetes 🚀

¡Es hora de poner a prueba lo que aprendiste! Eres el ingeniero de software principal del centro de lanzamiento espacial. Tu misión es escribir el programa que realiza la cuenta regresiva antes de que el cohete despegue.

### Instrucciones paso a paso:
1. Crea una variable llamada `cuenta` y asígnale el valor `10`. Esta será tu cuenta regresiva inicial.
2. Escribe un texto en pantalla que anuncie: `"Preparando lanzamiento..."`.
3. Crea un bucle `while` que siga repitiéndose **mientras** la variable `cuenta` sea mayor que `0`.
4. **Dentro del bucle** (recuerda la indentación):
   - Imprime el valor actual de la variable `cuenta`.
   - Resta `1` al valor de `cuenta` y vuelve a guardarlo en la misma variable.
5. **Fuera del bucle** (sin indentación, para que se ejecute solo al final):
   - Imprime el mensaje: `"¡Despegue! 🚀"`.

### Reglas estrictas:
- **Conceptos permitidos**: Variables, asignación (`=`), números enteros, resta (`-`), impresión en pantalla (`print`), bucle `while`, mayor que (`>`), dos puntos (`:`).
- **Prohibido**: No puedes usar la función `time.sleep()`, ni bucles `for`, ni trucos matemáticos avanzados como `-=`. Hazlo paso a paso. No uses palabras que no hayamos visto.

### Resultado esperado en la terminal:
```text
Preparando lanzamiento...
10
9
8
7
6
5
4
3
2
1
¡Despegue! 🚀
```
