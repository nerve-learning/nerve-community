# Teoría: Tu Cinturón de Herramientas 🛠️

Para el jefe final de este módulo no te enseñaré ningún concepto nuevo. Vamos a armar un rompecabezas usando todas las piezas que ya aprendiste a dominar.

Imagina que eres un detective organizando una escena del crimen. Estas son las herramientas que llevas en tu cinturón:

### 1. Los Ojos (`os`)
Necesitas ver qué hay en la habitación y saber cómo caminar.
- `os.listdir("carpeta")`: Te da una lista con los nombres de todos los archivos revueltos.
- `os.path.join(A, B)`: El pegamento mágico. Une el nombre de la carpeta y el nombre del archivo con la barra inclinada correcta (`/` o `\`), sin importar si estás en Windows o Mac.

### 2. Las Manos (`shutil`)
Necesitas levantar un archivo y ponerlo en otra caja.
- `shutil.move(origen, destino)`: Levanta el archivo de la ruta origen y lo suelta en la ruta destino.

### 3. La Red de Seguridad (`try / except`)
¿Qué pasa si intentas mover un archivo pero otro programa lo está usando y está bloqueado? No queremos que el robot organizador muera.
- Envuelves el `shutil.move()` en un `try:`. Si falla, saltará al `except Exception as e:` y el robot simplemente pasará al siguiente archivo.

### 4. La Libreta de Notas (`logging`)
El robot trabajará en silencio, pero debe dejarte un reporte de su jornada laboral.
- `logging.basicConfig(filename="reporte.log", level=logging.INFO)`: Prepara el cuaderno.
- `logging.info("Moví el archivo X")`: Anota sus éxitos.
- `logging.error("No pude mover el archivo Y")`: Anota sus tropiezos.

## Anatomía de una cadena: `.endswith()`
Solo un pequeño recordatorio de los módulos pasados. Para saber si un archivo es una foto o un texto, puedes usar el método de los textos llamado `.endswith()` (termina con).

```python
archivo = "vacaciones.jpg"
if archivo.endswith(".jpg"):
    print("¡Es una imagen!")
```
