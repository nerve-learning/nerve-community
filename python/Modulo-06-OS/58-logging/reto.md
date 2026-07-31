# Reto 58: El Diario del Robot Espacial 🤖

Acabas de programar la inteligencia artificial de un robot explorador de Marte. Como el robot está muy lejos, no puedes ver su pantalla. Necesitas que deje un registro escrito de todo lo que hace y de sus problemas, para que puedas leerlo cuando aterrice.

## El Objetivo
Escribir un script llamado `reto.py` que configure una bitácora y simule la actividad del robot, guardando distintos niveles de mensajes en un archivo de texto.

## Instrucciones Paso a Paso

1. Importa el módulo necesario para llevar una bitácora.
2. Configura el sistema (usando `basicConfig`) para que:
   - El archivo donde se guardará todo se llame `diario_robot.txt`.
   - El nivel mínimo de registro sea de Información (la etiqueta en mayúsculas).
3. Usa la función de escritura de **Información** para guardar el mensaje: `"El robot ha aterrizado en Marte."`
4. Usa la función de escritura de **Advertencia** para guardar el mensaje: `"Tormenta de arena detectada. Visibilidad reducida."`
5. Usa la función de escritura de **Error** para guardar el mensaje: `"¡Atasco! La rueda derecha no responde."`
6. Finalmente, pon un `print()` normal (para la pantalla de la Tierra) que diga: `"Simulación del robot terminada. Revisando la bitácora..."`

## Reglas Estrictas
- **Conceptos permitidos**: `import logging`, `logging.basicConfig(filename=..., level=...)`, `logging.INFO`, `logging.info()`, `logging.warning()`, `logging.error()`, `print()`.
- **Conceptos prohibidos**: Modificar el formato de los logs con `format=`, usar variables complejas, o enviar logs a la consola simultáneamente.

## Resultado Esperado

En tu **terminal** (pantalla), solo deberías ver:
```text
Simulación del robot terminada. Revisando la bitácora...
```

Pero si abres el archivo **`diario_robot.txt`**, deberías ver algo así:
```text
INFO:root:El robot ha aterrizado en Marte.
WARNING:root:Tormenta de arena detectada. Visibilidad reducida.
ERROR:root:¡Atasco! La rueda derecha no responde.
```
*(Nota: Python agrega automáticamente ese texto de `INFO:root:` al principio de las líneas).*
