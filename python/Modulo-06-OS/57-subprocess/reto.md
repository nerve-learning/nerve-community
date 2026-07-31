# Reto 57: El Calculador Invisible

Tu programa principal de Python va a utilizar a **otro** programa de Python para hacer matemáticas sin ensuciarse las manos.

## El Objetivo
Escribe un script llamado `reto.py` que invoque un subproceso para calcular una suma, atrape la respuesta y la imprima en pantalla.

## Las Instrucciones

1. Importa el módulo `subprocess`.
2. Crea una variable que ejecute `subprocess.run()`.
3. El comando que debes ejecutar en forma de lista es: `["python", "-c", "print(100 + 150)"]`
   - *(Nota: `-c` le dice a Python que ejecute el texto que le sigue como si fuera un mini-programa).*
4. Asegúrate de configurar `capture_output=True` y `text=True`.
5. Imprime un mensaje amigable seguido de la respuesta que el subproceso guardó en `.stdout`.

## Resultado Esperado

Al ejecutar tu script, deberías ver algo así:

```text
Solicitando un cálculo al subproceso...
El subproceso respondió que el resultado es:
250
```
