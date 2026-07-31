# Reto 82: El Registro de Calificaciones

Eres un profesor y necesitas pasar las notas de tus 3 alumnos de tu libreta de papel a un formato digital profesional para que la escuela lo pueda leer.

### Pasos a seguir:
1. Trae tu herramienta de tablas `pandas` y ponle su apodo `pd`.
2. Crea un diccionario llamado `boleta_calificaciones`.
3. Dentro del diccionario, crea tres columnas (llaves):
   - `"Alumno"` (con los nombres "Juan", "Maria", "Pedro").
   - `"Matematicas"` (con las notas 85, 95, 70).
   - `"Historia"` (con las notas 90, 88, 75).
4. Crea una variable llamada `registro_oficial`.
5. Usa `pd.DataFrame()` para convertir tu `boleta_calificaciones` en una tabla y guárdalo en `registro_oficial`.
6. Imprime en pantalla tu `registro_oficial`.

### Reglas estrictas:
- **PERMITIDO:** `import pandas as pd`, crear diccionarios `{}`, usar `pd.DataFrame()`, `print()`.
- **PROHIBIDO:** Usar Numpy, intentar imprimir las listas por separado sin crear el DataFrame. Todas las listas deben tener 3 elementos exactos.

### Resultado esperado en la terminal:
*(Nota: Pandas agregará automáticamente los números 0, 1 y 2 a la izquierda, eso es normal y se llama "índice").*
```text
  Alumno  Matematicas  Historia
0   Juan           85        90
1  Maria           95        88
2  Pedro           70        75
```
