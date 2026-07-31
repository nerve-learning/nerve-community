# CLI Personal Útil

> **Nivel**: Módulos 05–06 completados
> **Tiempo estimado**: 3 horas
> **Lenguaje**: Python

## Tu misión

Una CLI (herramienta de línea de comandos) que sea útil para tu vida real.

## Lo que debe hacer tu programa

- Tiene al menos 3 comandos distintos (ej: `add`, `list`, `remove`)
- Guarda datos en un archivo .txt o .json que persiste entre ejecuciones
- Muestra ayuda si no se pasan argumentos

## Restricciones (respétalas o el reto no cuenta)

- **Solo puedes usar** conceptos de los módulos 01 al 06
- **Obligatorio**: usar sys.argv para los comandos
- **Obligatorio**: al menos 3 funciones con docstring
- **No puedes usar**: argparse, click, typer
- **Obligatorio**: manejo de errores con try/except
- El programa debe correr con `python reto.py [comando]`

## Criterio de éxito

Tu solución es válida si:
1. La herramienta funciona entre sesiones (los datos persisten)
2. No crashea si le pasas argumentos inválidos
3. Alguien que no te conoce puede entender el output sin explicación
