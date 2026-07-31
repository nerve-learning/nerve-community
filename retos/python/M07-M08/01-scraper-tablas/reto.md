# Scraper de Tablas Útiles

> **Nivel**: Módulos 07–08 completados
> **Tiempo estimado**: 3 horas
> **Lenguaje**: Python

## Tu misión

Un scraper que extrae tablas de nuestra propia web comunitaria y las convierte en datos útiles.

## Lo que debe hacer tu programa

- Extrae al menos una tabla de **https://nerve.community.aleniastudios.me**
- Limpia los datos (quita caracteres raros, normaliza números)
- Permite filtrar la tabla por columna y valor
- Guarda el resultado en JSON

## Restricciones (respétalas o el reto no cuenta)

- **Solo puedes usar** conceptos de los módulos 01 al 08
- **Obligatorio**: BeautifulSoup
- **Obligatorio**: clases para representar los datos (mínimo una clase)
- **No puedes usar**: pandas, selenium
- El programa debe correr con `python reto.py` sin argumentos adicionales

## Criterio de éxito

Tu solución es válida si:
1. datos.json generado con estructura limpia
2. Los datos extraídos provienen de **nerve.community.aleniastudios.me**
3. Alguien que no te conoce puede entender el output sin explicación
