# Reto 59: El Lector Blindado 🛡️

En los niveles pasados aprendiste a leer archivos de texto usando `open()`. Pero, ¿qué pasa si le pides a Python que abra un archivo que alguien borró por accidente? Exacto, el programa explota.

Vamos a crear un lector de archivos que sea indestructible.

## El Objetivo
Escribe un script llamado `reto.py` que intente leer un archivo que NO existe. En lugar de que el programa muera, debe atrapar el error, avisarle al usuario de forma amigable y terminar con gracia.

## Instrucciones Paso a Paso

1. Crea un bloque `try:`.
2. Dentro del `try:`, crea una variable e intenta abrir un archivo llamado `"fantasma.txt"` en modo lectura (`"r"`). (Recuerda, este archivo no existe en tu carpeta, y eso es exactamente lo que queremos).
3. Crea un bloque `except Exception as e:` para colocar tu red de seguridad.
4. Dentro del bloque `except`, imprime un mensaje amigable que diga: `"Lo siento, no pudimos encontrar el archivo. Detalles del problema: "` seguido de la variable `e` que contiene el error real.
5. Finalmente, **fuera** de los bloques try/except, imprime el mensaje: `"El programa ha finalizado con elegancia."`

## Reglas Estrictas
- **Conceptos permitidos**: `try:`, `except Exception as e:`, `open()`, `print()`, variables.
- **Conceptos prohibidos**: Crear el archivo `fantasma.txt` (queremos que falle), múltiples bloques except, ciclos o funciones.

## Resultado Esperado

Al ejecutar tu script, tu terminal NO debe mostrar texto rojo aterrador. Debería verse exactamente así:

```text
Lo siento, no pudimos encontrar el archivo. Detalles del problema: [Errno 2] No such file or directory: 'fantasma.txt'
El programa ha finalizado con elegancia.
```
