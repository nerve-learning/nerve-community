# Reto 106: El Forjador de Llaves 🗝️

Tu base secreta requiere contraseñas nuevas cada semana y te han designado como el Maestro Forjador. Tu misión es crear un programa en Python que automáticamente imprima dos llaves maestras de alta seguridad en la pantalla para que tu equipo las elija.

## 📝 Instrucciones

Crea un archivo llamado `reto.py` y escribe código que:

1. Imprima un mensaje de bienvenida que diga: "¡Bienvenido a la Forja de Llaves!".
2. Use el módulo `os` para darle una orden a la terminal ejecutando el generador de claves de Nerve en modo **aleatorio** (`random`).
3. Imprima un texto bonito separador (ej. "--------------------------------").
4. Use el módulo `os` para darle otra orden a la terminal ejecutando el generador de claves en modo **frase** (`passphrase`).

### 🛑 Reglas Estrictas
* **Conceptos permitidos**: `import os`, `os.system()`, variables de texto y la función `print()`.
* **Prohibido**: Hacer ciclos (`for`, `while`) que no necesitamos aquí, o intentar capturar y guardar el texto de Nerve en variables dentro de Python. Como todavía no te he enseñado a capturar la respuesta de la terminal usando cosas avanzadas, ¡simplemente deja que `os.system` haga su magia y lo imprima directo en la pantalla!

### 🎯 Resultado Esperado en Terminal
Cuando ejecutes tu código, deberías ver algo así:

```text
¡Bienvenido a la Forja de Llaves!
Generando llave de símbolos...
[Aquí saldrán letras y números raros generados por Nerve en tu pantalla]
--------------------------------
Generando frase secreta fácil de recordar...
[Aquí saldrán palabras separadas por guiones generadas por Nerve en tu pantalla]
```
