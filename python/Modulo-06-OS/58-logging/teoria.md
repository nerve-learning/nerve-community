# Teoría: Escribiendo en el Diario (`logging`)

El módulo `logging` viene incluido en Python y nos permite clasificar nuestros mensajes por su nivel de gravedad o importancia, en lugar de simplemente "gritar" todo a la pantalla como hace `print()`.

Hay tres niveles principales de gravedad que debes conocer (de menor a mayor):
1. **INFO** (Información): "Todo va bien, solo te aviso que hice esto".
2. **WARNING** (Advertencia): "Ojo, algo raro pasó, pero puedo seguir trabajando".
3. **ERROR** (Error grave): "Algo salió mal y no pude terminar mi tarea".

## La Anatomía de `logging`

Antes de escribir en la bitácora, necesitamos preparar el cuaderno. Esto se hace una sola vez al principio de tu programa:

```python
import logging

logging.basicConfig(filename="bitacora.txt", level=logging.INFO)
```

**Desmontaje de los símbolos nuevos:**
- `basicConfig()`: Es la función que "prepara el cuaderno". (Basic Config = Configuración Básica).
- `filename="bitacora.txt"`: Le decimos exactamente cómo se llamará el archivo donde escribiremos nuestro diario. Si no existe, Python lo creará mágicamente por nosotros.
- `level=`: Le indicamos desde qué nivel de gravedad queremos empezar a guardar.
- `logging.INFO`: Es una "etiqueta" especial que vive dentro de la caja de `logging`. Al ponerla aquí, le decimos: *"Guarda desde el nivel de Información hacia arriba"*. (Es decir, guardará INFO, WARNING y ERROR). Si pusiéramos `logging.ERROR`, solo guardaría los errores y tiraría a la basura los mensajes de información. ¡Nota que `INFO` va en MAYÚSCULAS!

Una vez configurado el cuaderno, usamos los "lápices" de colores para escribir:

```python
logging.info("El usuario inició sesión.")
logging.warning("La contraseña es muy corta.")
logging.error("¡No hay internet!")
```
Cada uno de estos comandos guardará el mensaje en `bitacora.txt`, etiquetándolo automáticamente con la palabra INFO, WARNING o ERROR.

## ¿Qué pasa si me equivoco?

### Error Común 1: Usar `print` en lugar de `logging`
Si estás usando `print()` para registrar errores, nunca los encontrarás si cierras la pantalla. Usa `print()` solo para comunicarte con el usuario humano, y `logging` para dejar un rastro permanente para el programador (tú).

### Error Común 2: Escribir `.info` en mayúsculas o `.INFO` en minúsculas.
Las mayúsculas y minúsculas importan mucho.
- `logging.INFO` (todo mayúsculas) es el **NIVEL** (la etiqueta). Lo usas en `basicConfig`.
- `logging.info()` (todo minúsculas) es la **ACCIÓN** (la función). Lo usas para escribir un mensaje.

### Error Común 3: Olvidar `basicConfig`
Si olvidas poner la línea `logging.basicConfig(...)`, Python no sabrá en qué archivo escribir, así que por precaución simplemente arrojará tus mensajes de error a la pantalla y desechará los de información. ¡Siempre prepara tu cuaderno primero!
