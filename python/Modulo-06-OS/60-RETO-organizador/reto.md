# Reto 60: El Robot Organizador 🤖🧹

Es hora de la gran prueba. Vas a crear un script que limpie el desastre que dejó el programa `ejemplo.py`.

## El Objetivo
Escribir un script llamado `reto.py` que entre a la carpeta `"cuarto_desordenado"`, lea todos los archivos, los clasifique en imágenes o textos, los mueva a sus respectivas carpetas, y guarde un historial de todo en un archivo `.log`.

## Instrucciones Paso a Paso

1. **El Desastre**: Primero, ejecuta `ejemplo.py` para que se cree la carpeta `"cuarto_desordenado"` con sus archivos.
2. **Tu Script (`reto.py`)**:
   - Importa `os`, `shutil` y `logging`.
   - Configura el diario: usa `logging.basicConfig` para escribir en `"limpieza.log"` desde el nivel `INFO`.
   - Crea dos carpetas nuevas usando `os.makedirs()` (recuerda comprobar si ya existen con `os.path.exists()`): 
     - Una carpeta llamada `"cuarto_desordenado/imagenes"`
     - Otra llamada `"cuarto_desordenado/documentos"`
3. **El Ciclo de Limpieza**:
   - Usa `os.listdir("cuarto_desordenado")` para obtener la lista de cosas en el piso.
   - Inicia un ciclo `for` para agarrar cada cosa una por una.
4. **La Lógica**:
   - Para cada archivo, arma su ruta de origen (`os.path.join`).
   - Usa `if` para preguntar: ¿Termina en `.jpg`? Entonces arma su ruta de destino hacia la carpeta de imágenes. ¿Termina en `.txt`? Arma su ruta hacia los documentos. (Si es otra cosa, sáltalo o ignóralo).
   - Ignora también si lo que lees en el `for` es una carpeta (como "imagenes" o "documentos") usando `os.path.isfile(ruta_origen)`.
5. **El Movimiento**:
   - Envuelve el comando `shutil.move(origen, destino)` en un bloque `try:`.
   - Después de moverlo con éxito, anótalo en la bitácora: `logging.info("Archivo movido: " + nombre)`
   - Si algo sale mal, atrápalo con un `except Exception as e:` y anótalo: `logging.error("Fallo al mover: " + str(e))`

## Reglas Estrictas
- **Conceptos permitidos**: `os`, `shutil`, `logging`, `try / except`, ciclos `for`, condicionales `if/elif`, concatenación, `.endswith()`.
- **Conceptos prohibidos**: Programación orientada a objetos (clases), bibliotecas externas avanzadas como `pathlib` (nos apegamos a `os`), funciones complicadas si no las necesitas.

## Resultado Esperado

En la terminal no necesitas mostrar mucho, tal vez un `"Limpieza terminada"`.
El verdadero resultado será:
1. La carpeta `cuarto_desordenado` estará vacía de archivos sueltos, y solo tendrá dos subcarpetas (`imagenes` y `documentos`) con los archivos adentro.
2. Aparecerá un archivo `limpieza.log` con un texto similar a:
```text
INFO:root:Archivo movido: meme.jpg
INFO:root:Archivo movido: receta_pastel.txt
...
```
