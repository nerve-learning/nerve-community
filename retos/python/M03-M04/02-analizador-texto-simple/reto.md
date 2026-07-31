# Analizador de Texto Simple

> **Nivel**: Módulos 03–04 completados
> **Tiempo estimado**: 2 horas
> **Lenguaje**: Python

## Tu misión

Un programa que analiza un texto largo (mínimo 100 palabras, hardcoded) y produce un reporte.

## Lo que debe hacer tu programa

- Cuenta palabras totales, únicas y repetidas
- Encuentra la palabra más larga y la más corta
- Lista las 5 palabras más frecuentes (sin contar "el", "la", "de", "que", "y")
- Detecta si es un texto "rico" (>50% palabras únicas) o "repetitivo"

## Restricciones (respétalas o el reto no cuenta)

- **Solo puedes usar** conceptos de los módulos 01 al 04
- **Obligatorio**: usar sets para palabras únicas
- **Obligatorio**: usar diccionarios para frecuencias
- **No puedes usar**: import collections, pandas, nltk
- El programa debe correr con `python reto.py` sin argumentos adicionales

## Criterio de éxito

Tu solución es válida si:
1. Genera un reporte con todas las métricas
2. Las frecuencias están correctas y filtradas
3. Alguien que no te conoce puede entender el output sin explicación
