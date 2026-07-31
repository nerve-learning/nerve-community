# Reto 34: El Detector de Intrusos 🚨

Eres el administrador de seguridad del servidor principal. Tienes una lista con los códigos de acceso de las personas que están entrando al sistema. Te acaban de informar que un intruso usará el código `"HACKER"`. Tu trabajo es detener el análisis del servidor inmediatamente en cuanto detectes ese código.

### Instrucciones paso a paso:
1. Crea una lista llamada `accesos` con estos textos exactos: `"admin"`, `"usuario1"`, `"HACKER"`, `"invitado"`, `"usuario2"`.
2. Imprime un mensaje que diga `"Analizando accesos al servidor..."`.
3. Crea un bucle `for` que recorra la lista `accesos` usando una variable temporal llamada `codigo`.
4. **Dentro del bucle `for`** (primer nivel de indentación):
   - Imprime el texto `"Revisando:"` y en la siguiente línea imprime la variable `codigo`.
   - Agrega un bloque `if` que compruebe si el `codigo` es exactamente igual (`==`) a `"HACKER"`.
   - **Dentro de ese `if`** (segundo nivel de indentación), imprime: `"¡INTRUSO DETECTADO! Apagando sistema..."`.
   - Inmediatamente después del mensaje, usa el freno de emergencia para detener el bucle.
5. **Fuera del bucle** (sin indentación), imprime: `"Servidor fuera de línea."`.

### Reglas estrictas:
- **Conceptos permitidos**: Variables, cadenas de texto (`""`), listas (`[]`), bucle `for`, palabra `in`, condicional `if`, igualdad (`==`), función `print`, palabra `break`, dos puntos (`:`), indentación.
- **Prohibido**: No puedes usar `while`, `continue`, ni funciones para borrar elementos de la lista. Debes detener la búsqueda en el instante preciso.

### Resultado esperado en la terminal:
```text
Analizando accesos al servidor...
Revisando:
admin
Revisando:
usuario1
Revisando:
HACKER
¡INTRUSO DETECTADO! Apagando sistema...
Servidor fuera de línea.
```
