# Procesador de CSV

> **Nivel**: Módulos 05–06 completados
> **Tiempo estimado**: 3 horas
> **Lenguaje**: Python

## Tu misión

Un script que descarga, procesa y resume datos de un archivo CSV público.

## Lo que debe hacer tu programa

- Lee un CSV real de internet (usa cualquier dataset público de kaggle, datos.gob.mx, etc.)
- Limpia los datos (elimina filas vacías, normaliza texto)
- Genera un reporte: mínimo, máximo, promedio de al menos 2 columnas numéricas
- Guarda el reporte limpio en un nuevo CSV

## Restricciones (respétalas o el reto no cuenta)

- **Solo puedes usar** conceptos de los módulos 01 al 06
- **No puedes usar**: pandas, numpy
- **Obligatorio**: módulo csv de la librería estándar
- **Obligatorio**: módulo requests para la descarga
- **Obligatorio**: al menos 4 funciones separadas
- El programa debe correr con `python reto.py` sin argumentos adicionales

## Criterio de éxito

Tu solución es válida si:
1. reporte_limpio.csv generado correctamente
2. reporte impreso en consola con las métricas correctas
3. Alguien que no te conoce puede entender el output sin explicación
